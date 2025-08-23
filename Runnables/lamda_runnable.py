from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnablePassthrough,RunnableParallel,RunnableLambda

load_dotenv()

def word_count(text):
    return len(text.split())

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

joke_chain=RunnableSequence(prompt,model,parser)

parallel_chain=RunnableParallel(
    {
        "joke":RunnablePassthrough(),
        "word_count":RunnableLambda(word_count)
    }
)

final_chain=RunnableSequence(joke_chain,parallel_chain)

result=final_chain.invoke({"topic":"ai"})

print(result)