from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv() 
model=ChatOpenAI()

parser=StrOutputParser()

class Feedback(BaseModel):
    
    sentiment:Literal["Positive","Negative"]=Field(description="Give the sentiment of the feedback")

parser2=PydanticOutputParser(pydantic_object=Feedback)

prompt1=PromptTemplate(
    template="classfy the sentiment of following feedback text into positive or negative \n {feedback} \n{format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction":parser2.get_format_instructions()}
)

classifier_chain=prompt1|model|parser2

prompt2=PromptTemplate(
    template="Write a appropate respose to this positive feedback \n {feedback} ",
    input_variables=["feedback"]
)
prompt3=PromptTemplate(
    template="Write a appropate respose to this negative feedback \n {feedback} ",
    input_variables=["feedback"]
)
chain1=prompt2|model|parser
chain2=prompt3|model|parser

brach_chain=RunnableBranch(
    (lambda x:x["sentiment"]=="positive",chain1),
    (lambda x:x["sentiment"]=="negative",chain1),
    RunnableLambda(lambda x:"could not find sentiment")  # it defult chain it run if above 2 are false
)

chain=classifier_chain|brach_chain

result=chain.invoke({"feedback":"perfect phone to buy"})

print(result)