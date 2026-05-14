from langchain_core.prompts import ChatPromptTemplate,FewShotChatMessagePromptTemplate
# Examples
examples = [
    {"input": "AI", "output": "Artificial Intelligence"},
    {"input": "ML", "output": "Machine Learning"},
]
# Example prompt
example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{output}"),
])
# Few-shot template
few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
)
# Print
print(few_shot_prompt.format_messages())  