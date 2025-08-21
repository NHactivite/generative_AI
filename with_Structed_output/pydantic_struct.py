from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Optional,Literal
from pydantic import BaseModel,Field
load_dotenv()
model=ChatOpenAI()
# output schema 

class Review(BaseModel):
     key_themes: list[str] =Field(description="write down the key themes discuss in the review")
     summary:str =Field(description="write down summary the review")
     sentiment:Literal["pos","neg"] =Field(description="write down sentiment the review")
     pros:Optional[list[str]]= Field(description="write down the all the pros inside the list",default=None)
     cons:Optional[list[str]]= Field(description="write down the all the cons inside the list",default=None)

struct_model=model.with_structured_output(Review)

result=struct_model.invoke("""I’ve been using these headphones for a month now, and the sound quality is simply outstanding.
The noise cancellation blocks out almost everything, making it perfect for work and travel.
Battery life easily lasts for days on a single charge but use 1-2 hours continous it have appear heating issue.
The design is lightweight and very comfortable, even during long sessions.
Definitely worth the investment if you want premium audio and peace of mind""")

print(result)
print(result.summary)
print(result.sentiment)