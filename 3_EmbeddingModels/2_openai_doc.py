from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeding=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

documents=[
    "Delhi is the capital of india",
    "paris is the capital of france",
    "thimphu is the capital of bhutan"
]

result=embeding.embed_documents(documents)
print(str(result))

 