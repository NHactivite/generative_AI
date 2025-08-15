from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model="gpt-4");

result=model.invoke("how Donald Trump look like in one line",temperature=1.5,max_completion_tokens=10)

# print(result)
print(result.content)