from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional
load_dotenv()
model=ChatOpenAI()
# output schema 

class Review(TypedDict):
     key_themes:Annotated[list[str],"write down the key themes discuss in the review"]
     summary:str   # here also use Annotated[str,"write down the summary of the review"]   
     sentiment:str  # here also use Annotated[str,"write down the sentiment of the review"]   
     pros:Annotated[Optional[list[str]],"write down the all the pros inside the list"]
     cons:Annotated[Optional[list[str]],"write down the all the cons inside the list"]



struct_model=model.with_structured_output(Review)

result=struct_model.invoke("""I’ve been using these headphones for a month now, and the sound quality is simply outstanding.
The noise cancellation blocks out almost everything, making it perfect for work and travel.
Battery life easily lasts for days on a single charge but use 1-2 hours continous it have appear heating issue.
The design is lightweight and very comfortable, even during long sessions.
Definitely worth the investment if you want premium audio and peace of mind""")

print(result)
print(result["summary"])
print(result["sentiment"])