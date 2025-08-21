from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()

model=ChatOpenAI()

parser=JsonOutputParser()

template1= PromptTemplate(
    template="give me the name,age and city of a frictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

# without chain---------------------------------------
# promt=template1.format()
# result=model.invoke(promt)
# final_result=parser.parse(result.content)

# with Chain-----------------------------------------------
chain=template1|model|parser
final_result=chain.invoke({})

print(final_result)

