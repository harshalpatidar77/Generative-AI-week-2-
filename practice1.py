from dotenv import load_dotenv 
import os 
from groq_demo import ChatGroq 
# load variables from .env 
load_dotenv() 
# get API key from .env 
groq_api_key = os.getenv("GROQ_API_KEY") 
# create LLM Model 
llm = ChatGroq(api_key = groq_api_key, model = "llama-3.1-8b-instant") 
# user question 
while(True):
    print("press 1 for ask query") 
    print("print 2 for exit") 
    a=int(input()) 
    if a==1:
        question = input("enter your query") 
        response = llm.invoke(question) 
        print(response.content)  
    elif a==2:
        break 