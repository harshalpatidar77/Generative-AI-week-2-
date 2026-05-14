from dotenv import load_dotenv 
import os 
from groq_demo import ChatGroq 
# load variables from .env 
load_dotenv() 
# get API key from .env 
groq_api_key = os.getenv("GROQ_API_KEY") 
# create LLM 
llm = ChatGroq(api_key = groq_api_key,model = "llama-3.1-8b-instant") 
# user question 
question = "describe about Paris?" 
# get response 
response = llm.invoke(question) 
# print response 
print(response.content)  

