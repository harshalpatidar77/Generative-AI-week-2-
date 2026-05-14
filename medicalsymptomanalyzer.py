from dotenv import load_dotenv 
from langchain_groq import ChatGroq 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 
# load api key from .env 
load_dotenv() 
# create groq model 
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0 
) 
# prompt template 
prompt = ChatPromptTemplate.from_template("""
You are a medical assistant of doctor which is specialized in MBBS & MD.
Analyze the following symptoms:
{symptoms}
Give:
1. Possible condition
2. Basic precautions
3. Suggest whether doctor consultation is needed 
4. Suggest treatment 
5. Suggest medicine  
do not give the medicine more than 3 
suggest for a diagnosis report if required 
Keep the answer short and simple.                                         
""") 
# output parser 
parser = StrOutputParser() 
# chain 
chain = prompt | llm | parser 
# user input 
user_symptoms = input("Enter your symptoms:") 
# Run chain
response = chain.invoke({
    "symptoms": user_symptoms
}) 
# Print result
print("\nMedical Analysis:\n")
print(response) 
