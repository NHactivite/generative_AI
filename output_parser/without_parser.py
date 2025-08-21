from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

model=ChatOpenAI()

template1= PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"]
)
template2= PromptTemplate(
    template="write a 5 line summary on the following text. /n {text}",
    input_variables=["text"]
)

prompt1=template1.invoke({"topic":"black hole"})
result=model.invoke(prompt1)
prompt2=template2.invoke({"text":result.content})
final_Result=model.invoke(prompt2)

print(final_Result)