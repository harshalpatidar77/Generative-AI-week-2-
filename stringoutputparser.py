from dotenv import load_dotenv 
from langchain_groq import ChatGroq 
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser   
# load .env file 
load_dotenv() 
# LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant"
)  
# Prompt template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words."
) 
# string output parser 
parser = StrOutputParser() 
# chain 
chain = prompt | llm | parser 
# run chain 
response = chain.invoke({
    "topic": "Artificial Intelligence"
}) 
# Print output
print(response) 