
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Optional,Literal
from pydantic import BaseModel,Field
import json
load_dotenv()
model=ChatOpenAI()
# output schema 


json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer",
       "default": "Anonymous"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}

struct_model=model.with_structured_output(json_schema)

result=struct_model.invoke("""I’ve been using these headphones for a month now, and the sound quality is simply outstanding.
The noise cancellation blocks out almost everything, making it perfect for work and travel.
Battery life easily lasts for days on a single charge but use 1-2 hours continous it have appear heating issue.
The design is lightweight and very comfortable, even during long sessions.
Definitely worth the investment if you want premium audio and peace of mind""")

print(result)
print(json.dumps(result, indent=2))