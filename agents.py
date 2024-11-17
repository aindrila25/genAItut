from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.utilities import ArxivAPIWrapper
from langchain.agents import load_tools
from langchain_core.prompts import ChatPromptTemplate
from langgraph.prebuilt import create_react_agent




load_dotenv()
def generate_papersummary(code):
    llm = ChatGroq(model ="llama3-groq-8b-8192-tool-use-preview")
    tools = load_tools(["arxiv","wikipedia"]) #wikipedia is used to give the meanings of complicated terms that are used in arxiv
    prompt= ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant that takes an arxiv paper code and simplifies it to give an explanation quoting articles from wikipedia for the more complicated terms" ),
        ("human","The arxiv paper code is {code}")
    ]
)
    agent = create_react_agent(
    llm , tools
)
    
    initial_messages = prompt.invoke({"code":code}).to_messages()
    messages=agent.invoke(input={"messages": initial_messages})
    for index , msg in enumerate (messages["messages"]):
        print (msg.content)
    return messages["messages"][-1].content

