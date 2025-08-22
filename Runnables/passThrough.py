from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnablePassthrough,RunnableParallel

load_dotenv()

prompt=PromptTemplate(
    template="write a joke of the following topic \n {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="Explain the following joke \n {text}",
    input_variables=["text"]
)

model=ChatOpenAI()

parser=StrOutputParser()

joke_gen_chain=RunnableSequence(prompt,model,parser)

parallel_chain=RunnableParallel({
    "joke":RunnablePassthrough(),  # it same input as a output , in this case it hold joke 
    "explanation":RunnableSequence(prompt2,model,parser)
})

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)
result=final_chain.invoke({"topic":"black hole"})

print(result)