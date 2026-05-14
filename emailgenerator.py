from dotenv import load_dotenv 
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 
# Load .env
load_dotenv()
# Groq model
llm = ChatGroq(
    model="llama-3.1-8b-instant"
) 
# Prompt template
prompt = ChatPromptTemplate.from_template(
    """
Write a professional email.
Topic: {topic}
Keep the email short and clear.
"""
) 
# Output parser
parser = StrOutputParser()
# Simple chain
chain = prompt | llm | parser    
# User input
topic = input("Enter email topic: ")
# Run chain
response = chain.invoke({
    "topic": topic
})  
# Print output
print("\nGenerated Email:\n")
print(response)      