from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load .env
load_dotenv()

# LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

# Output parser
parser = StrOutputParser()

# First prompt
prompt1 = ChatPromptTemplate.from_template(
    "Explain {topic} in one short paragraph."
)

# Second prompt
prompt2 = ChatPromptTemplate.from_template(
    "Summarize this text in 3 lines:\n{text}"
)

# First chain
chain1 = prompt1 | llm | parser

# Second chain
chain2 = prompt2 | llm | parser

# Sequential chain
topic = "Machine Learning and Deep Learning"

# Run first chain
result1 = chain1.invoke({"topic": topic})

# Run second chain
result2 = chain2.invoke({"text": result1})

# Print output
print("Explanation:\n")
print(result1)

print("\nSummary:\n")
print(result2)   