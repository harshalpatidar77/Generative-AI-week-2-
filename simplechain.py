from langchain_core.prompts import ChatPromptTemplate 
from langchain_groq import ChatGroq 
from dotenv import load_dotenv 
import os 
# load .env 
load_dotenv() 
# prompt 
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words"
) 
# Check API key
print(os.getenv("GROQ_API_KEY"))
# LLM 
llm = ChatGroq(
    api_key= os.getenv("GROQ_API_KEY"), 
    model = "llama-3.1-8b-instant"
) 
# Create chain 
chain = prompt | llm 
# invoke chain 
response = chain.invoke({
    "topic": "Transformers"
}) 
print(response.content)   