from dotenv import load_dotenv 
from langchain_groq import ChatGroq 
from langchain_core.messages import HumanMessage, AIMessage 
# Load .env
load_dotenv()
# LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant"
) 
# conversational messages 
messages = [
    HumanMessage(content="Hi"), 
] 
# first response 
response1 = llm.invoke(messages)
print("AI:", response1.content) 
# Add AI response to conversation 
messages.append(AIMessage(content=response1.content)) 
# user next message 
messages.append(
    HumanMessage(content="What is Machine Learning?") 
) 
# Second response
response2 = llm.invoke(messages)
print("\nAI:", response2.content) 
# Continue conversation
messages.append(AIMessage(content=response2.content))
messages.append(
    HumanMessage(content="Explain it in simple words")
) 
# Third response 
response3 = llm.invoke(messages)
print("\nAI:", response3.content) 