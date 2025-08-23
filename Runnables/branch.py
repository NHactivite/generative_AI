from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableBranch,RunnableSequence,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


load_dotenv() 
model=ChatOpenAI()

prompt1=PromptTemplate(
    template="write a detailed report on \n {topic}",
    input_variables=["topic"]
)


prompt2=PromptTemplate(
    template="summarized the following \n {topic}",
    input_variables=["topic"]
)

parser=StrOutputParser()

report_gen_chain=RunnableSequence(prompt1,model,parser)

branch_chain=RunnableBranch(
    (lambda x:len(x.split())>100,RunnableSequence(prompt2,model,parser)),
     RunnablePassthrough()
)

final_chain=RunnableSequence(report_gen_chain,branch_chain)

result=final_chain.invoke({"topic":"leg day"})

print(result)