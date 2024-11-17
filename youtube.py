import os
from dotenv import load_dotenv
from langchain_community.embeddings import JinaEmbeddings
from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain.vectorstores import FAISS
from langchain_groq import ChatGroq

load_dotenv()

embeddings = JinaEmbeddings(model_name="jina-embeddings-v2-base-en",jina_api_key=os.environ["JINA_API_KEY"])

def create_vector_db_from_youtube_url(video_url:str)->FAISS:
        loader = YoutubeLoader.from_youtube_url(video_url,language=["en-IN"])
        transcript = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100 )
        docs = text_splitter.split_documents(transcript) 
        db = FAISS.from_documents(docs,embeddings)
        return db

# print (create_vector_db_from_youtube_url)
def get_response_from_query(db,query,k=4):
        docs = db.similarity_search(query,k=k)
        docs_pages_content = " ".join([d.page_content for d in docs]) 
        llm =  ChatGroq(temperature=0.0,model="llama3-groq-8b-8192-tool-use-preview") 
        prompt = ChatPromptTemplate.from_messages(
        [

            (
                "system",
                "You are a helpful assistant that that can answer questions about youtube videos  based on the video's transcript."
                "Only use the factual information from the transcript to answer the question."
        
                "If you feel like you don't have enough information to answer the question, say \"I do not know .\""
                "Your answers should be verbose and detailed."
     ),
            (
               "human"," Answer the following question: {question}"
                "By searching the following video transcript: {docs}"
            )
        ]
    )   
        chain = prompt |llm
        ch=chain.invoke(
        {
            "question":query,
            "docs":docs_pages_content
        }
    )
        return ch.content

if __name__ == "__main__" :
    db =  create_vector_db_from_youtube_url("https://youtu.be/sXmrh4fJoaE?si=aAIFFm3iOE1eAC-X") 
    query = input("enter the question:")
    q = get_response_from_query(db,query)
    print (q)










# example of indexing    RAG   SEMI RAG