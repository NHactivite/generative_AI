from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.schema.runnable import RunnableParallel

load_dotenv()


llm=HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)
 
model1=ChatOpenAI()
model2= ChatHuggingFace(llm=llm)

prompt1=PromptTemplate(
    template="provide the short and simple note of following topic \n {topic}",
    input_variables=["topic"]
)

prompt2=PromptTemplate(
    template="genarate 5 short question answer from the following topic \n{topic}",
    input_variables=["topic"]
)

prompt3=PromptTemplate(
    template="marge the following notes and quiz into a single document \n notes-> {notes} and quiz->{quiz}",
    input_variables=["notes","quiz"]
)

parser=StrOutputParser()

parallel_chain=RunnableParallel({
    "notes":prompt1|model1|parser,
    "quiz":prompt2|model2|parser
})

merge_chain=prompt3|model1|parser


chain=parallel_chain|merge_chain

result=chain.invoke("why if we go any direction in inside a black hole is always go to  singularity ")

print(result)

chain.get_graph().print_ascii()