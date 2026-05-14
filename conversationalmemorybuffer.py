from dotenv import load_dotenv  
from langchain_groq import ChatGroq 
from langchain_core.messages import HumanMessage, AIMessage 
# load .env 
load_dotenv() 
# LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant"
) 
# window size 
k = 3 
# chat history 
chat_history = [] 
# chat loop 
while True:
    user_input = input("You: ") 
    if user_input.lower() == "exit":
        break 
    # add user message 
    chat_history.append(
        HumanMessage(content=user_input) 
    ) 
    # Keep only last k conversations
    window_memory = chat_history[-(k * 2):]  
    # invoke model 
    response = llm.invoke(window_memory) 
    # print message 
    print("AI:", response.content) 
    # Save AI response
    chat_history.append(
        AIMessage(content=response.content)
    )    
    # Print last 3 interactions
    print("\nLast 3 Interactions:\n") 
    for msg in window_memory: 
        if isinstance(msg, HumanMessage): 
            print("You:", msg.content) 
        elif isinstance(msg, AIMessage): 
            print("AI:", msg.content) 
    print("\n" + "-" * 50) 
    