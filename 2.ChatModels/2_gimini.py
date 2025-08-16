from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv();

model=ChatGoogleGenerativeAI(model="gemini-1.5-flash")

result=model.invoke("who is the vic chancallar of sibsagar university")
print(result.content)