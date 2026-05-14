from dotenv import load_dotenv 
from langchain_groq import ChatGroq 
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import JsonOutputParser  
# load .env file 
load_dotenv() 
# LLM 
llm = ChatGroq(
    model="llama-3.1-8b-instant"
) 
# JSON Parser
parser = JsonOutputParser() 
# Prompt
prompt = ChatPromptTemplate.from_template(
    """
Extract the following information from the paragraph:
- name
- gender
- age
Return the output only in valid JSON format.
Paragraph:
{paragraph}
"""
)   
# chain 
chain = prompt | llm | parser 
# Input paragraph
text = """
Rahul Sharma is a 22 year old male student who lives in Delhi.
"""
# Invoke chain
response = chain.invoke({
    "paragraph": text
}) 
# Print JSON output
print(response)  