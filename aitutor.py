from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# Load API key from .env
load_dotenv()
# Create Groq model
llm = ChatGroq(
    model="llama-3.1-8b-instant",
)
# Prompt template
prompt = ChatPromptTemplate.from_template(
    """
You are an AI Tutor.

Explain the following topic in simple and easy words:

Topic: {topic}
"""
)
# Output parser
parser = StrOutputParser()
# Simple chain
chain = prompt | llm | parser
# User input     
topic = input("Enter topic: ")
# Run chain
response = chain.invoke({
    "topic": topic
})
# Print output
print("\nAI Tutor Response:\n")
print(response)