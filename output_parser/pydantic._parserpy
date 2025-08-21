from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
load_dotenv()
model=ChatOpenAI()


class Person(BaseModel):
    name: str =Field(description="Name of the person"),
    age: int = Field(gt=18,description="age of the person"),
    city:str =Field(description="name of person city")

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template="generate the name, age and city of fictional character of {place} \n {format_instruction}",
    input_variables=["place"],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

# prompt= template.invoke({"place":"nepal"})
# result=model.invoke(prompt)
# final_result=parser.parse(result.content)

chain=template|model|parser
final_result=chain.invoke({"place":"sivasagar"})

print(final_result)