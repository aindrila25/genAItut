from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import load_tools
from langchain_core.prompts import ChatPromptTemplate
from langgraph.prebuilt import create_react_agent

load_dotenv()
def generate_mcq(topic,number):
    llm = ChatGroq(model ="llama3-groq-8b-8192-tool-use-preview")
    tools = load_tools(["wikipedia"]) 
    prompt= ChatPromptTemplate.from_messages(
    [
        (
        "system",
        "Generate  multiple-choice questions about the topic"
        "covering all the core and important topics."
        "Each question should have one correct answer and rest incorrect"
        ),
        (
        "human",
        "The topic is {topic}"
        "The number of questions it should generate are {number}"
        )
    ]
)
    agent = create_react_agent(
    llm , tools
)
    
    initial_messages = prompt.invoke({"topic":topic,"number": number}).to_messages()
    messages =agent.invoke(input={"messages": initial_messages})
    return messages["messages"][-1].content