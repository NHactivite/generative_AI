from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI()

messages=[
    SystemMessage(content="you are a helpfull assistant"),
    HumanMessage(content="tell me about python language")
]

result=model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)