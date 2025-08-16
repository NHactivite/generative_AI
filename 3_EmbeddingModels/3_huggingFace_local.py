from langchain_huggingface import HuggingFaceEmbeddings

embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# text="Delhi is the capital of india"
documents=[
    "Delhi is the capital of india",
    "paris is the capital of france",
    "thimphu is the capital of bhutan"
]

# vector=embeddings.embed_query(text)
vector=embeddings.embed_documents(documents)

print(str(vector))