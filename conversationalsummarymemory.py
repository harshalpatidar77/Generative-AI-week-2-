from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
# Load .env
load_dotenv()
# LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant"
)
# Chat history
chat_history = []
# Conversation summary
summary = ""
# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    # Add user message
    chat_history.append(
        HumanMessage(content=user_input)
    )
    # Create messages with summary
    messages = []
    if summary:
        messages.append(
            HumanMessage(
                content=f"Conversation Summary:\n{summary}"
            )
        )
    messages.extend(chat_history)
    # Invoke model
    response = llm.invoke(messages)
    # Print AI response
    print("AI:", response.content)
    # Save AI response
    chat_history.append(
        AIMessage(content=response.content)
    )
    # Update summary
    summary_prompt = f"""
    Summarize this conversation briefly:
    {chat_history}
    """
    summary_response = llm.invoke(summary_prompt)
    summary = summary_response.content
    # Print summary
    print("\nConversation Summary:")
    print(summary)
    print("\n" + "-" * 50) 
