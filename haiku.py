from langchain_groq import ChatGroq 
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv() #environment loader

def generate_haiku(language,topic):
    llm=ChatGroq(temperature=0.8,model="llama3-groq-8b-8192-tool-use-preview")
   # messages=[("system","You are a helpful assistant that suggests names for pets"),("human","Suggest {number} cool names for my pet")]
    prompt = ChatPromptTemplate.from_messages(
        [

            (
                "system",
                "You are a helpful assistant that gives great haiku to read."
"If the haiku is requested in a language other than English, no translations or extra text should be provided. Only the haiku should be returned in the target language."   
"Just keep responses in non-English languages minimal (just the haiku itself)."   
"Do not give any translations"      ),
            (
               "human","Write a haiku in {language} language and on the {topic}. " 
            )
        ]
    )
#name=llm.invoke(messages)
    chain = prompt |llm
    ch=chain.invoke(
        {
            "language":language,
            "topic": topic
        }
    )
    return ch.content
if __name__ == "__main__" :
    print(generate_haiku("English","Autumn"))