from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv 
import os 
load_dotenv() 
llm = ChatOpenAI(
    api_key = os.getenv('CEREBRAS_API_KEY'), 
    base_url = "https://api.cerebras.ai/v1",
    model = "llama3.1-8b" 
) 
response = llm.invoke("Explain transformers") 
print(response.content) 



