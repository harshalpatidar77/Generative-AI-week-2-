from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an HR interviewer. Ask professional interview questions."),
    ("human", "{role}")
])
messages = prompt.format_messages(
    role="Python Developer"
)
print(messages) 