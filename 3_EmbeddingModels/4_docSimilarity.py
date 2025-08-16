from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeding=OpenAIEmbeddings(model="text-embedding-3-large",dimensions=300)

document=[
    "Delhi is the capital of India.",
"New Delhi serves as the political center of the country.",
"delhi have highest population",
"assam present in north-est india",
"large population in assam",
"Mumbai is the financial hub of India.",
"Kolkata is famous for its cultural heritage.",
"in india mumbai also have large population"
]


query="which state have large population among all state in north-east india"

doc_embedding=embeding.embed_documents(document)
query_embeding=embeding.embed_query(query)

scores=cosine_similarity([query_embeding],doc_embedding)[0]

print(scores)
# index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
index, score = max(enumerate(scores), key=lambda x: x[1])

print(document[index])