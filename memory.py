from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.memory import ConversationBufferMemory

# Load .env
load_dotenv()

# LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

# Memory
memory = ConversationBufferMemory(
    return_messages=True
)

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# Parser
parser = StrOutputParser()

# Chain
chain = prompt | llm | parser

# Chat loop
while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # Load memory
    history = memory.load_memory_variables({})["history"]

    # Invoke chain
    response = chain.invoke({
        "history": history,
        "input": user_input
    })

    print("AI:", response)

    # Save memory
    memory.save_context(
        {"input": user_input},
        {"output": response}
    ) 