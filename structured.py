from typing import List, Optional
from pydantic import BaseModel,Field
from mcq import generate_mcq
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

class MCQ(BaseModel):
    """Multiple choice question"""
    
    question :str= Field(description="The question for the multiple choice question.")
    options  : List[str]= Field(description="The array of four options,out of which one will be correct and rest will be incorrect.")
    answer : int = Field(description="The index of the correct answer in the previous options list.The value must be 0 or 1 or 2 or 3.")

class MCQ_List(BaseModel):
    """List of Multiple choice question"""

    mcqs : List[MCQ] = Field(description="An array of Multiple choice questions.")

def generate_mcq_st(topic,n):
    llm = ChatGroq(model ="llama3-groq-8b-8192-tool-use-preview")
    ques_str = generate_mcq(topic,n)
    structured_llm = llm.with_structured_output(MCQ_List)
    st=structured_llm.invoke("Trandform the following questions into the given schema " + ques_str)
    return st

if __name__ == "__main__" :
    print(generate_mcq_st("python","5"))
