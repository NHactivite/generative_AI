from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema
load_dotenv()

model=ChatOpenAI()

schema=[
    ResponseSchema(name="fact_1",description="writw about fact_1"),
    ResponseSchema(name="fact_2",description="writw about fact_2"),
    ResponseSchema(name="fact_3",description="writw about fact_3"),
    ResponseSchema(name="fact_4",description="writw about fact_4")
]
parser = StructuredOutputParser.from_response_schemas(schema)

template1= PromptTemplate(
    template="give me 4 fact following topic \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

# prompt=template1.invoke({"topic":"black hole"})
# result=model.invoke(prompt)
# final_result=parser.parse(result.content)

chain=template1|model|parser
final_result=chain.invoke({"topic":"black hole"})

print(final_result)

