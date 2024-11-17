# from langchain.llms import Groq
from langchain_groq import ChatGroq 
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv() #environment loader

def generate_name(number,type):
    llm=ChatGroq(temperature=0.8,model="mixtral-8x7b-32768")  
   # messages=[("system","You are a helpful assistant that suggests names for pets"),("human","Suggest {number} cool names for my pet")]
    prompt = ChatPromptTemplate.from_messages(
        [

            (
                "system",
                "You are a helpful assistant that suggests names for pets"
            ),
            (
               "human","Suggest {number} cool names for my {name} " 
            )
        ]
    )

    #name=llm.invoke(messages)

 
    chain = prompt |llm
    ch=chain.invoke(
        {
            "number":number,
            "name":type
        }
    )
    return ch.content

if __name__ == "__main__" :

    print(generate_name("5","boy"))