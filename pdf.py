import os
from dotenv import load_dotenv
from langchain_community.embeddings import JinaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
import asyncio 

load_dotenv()

embeddings = JinaEmbeddings(model_name="jina-embeddings-v2-base-en",jina_api_key=os.environ["JINA_API_KEY"])

async def create_vector_db_from_pdf(file_path:str):
        loader = PyPDFLoader(file_path)
        pages = []
        async for page in loader.alazy_load():
            pages.append(page)
        return pages

def get_response_from_PDF(pages,number):
        docs_pages_content = " ".join([d.page_content for d in pages]) 
        llm =  ChatGroq(temperature=0.0,model="llama3-groq-8b-8192-tool-use-preview") 
        prompt = ChatPromptTemplate.from_messages(
        [

            (
                "system",
                "You are a helpful assistant that that can summarize  the pdf."
                "Make the summary accurate."
     ),
            (
               "human","This is the pdf content : {content}"
               "The maximum word limit should be : {number}"
            )
        ]
    )   
        chain = prompt |llm
        ch=chain.invoke(
        {
            "content":docs_pages_content,
            "number": number
          
        }
    )
        return ch.content
async def main():
    pages =  await create_vector_db_from_pdf("/home/aindrila/genAItut/3.pdf") 
    number = input("enter the  maximum number of words:")
    q = get_response_from_PDF(pages ,number )
    print (q)

if __name__ == "__main__" :
      asyncio.run(main())

    









# example of indexing    RAG   SEMI RAG