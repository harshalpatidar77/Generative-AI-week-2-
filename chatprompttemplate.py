from langchain_core.prompts import ChatPromptTemplate 
# create chat prompt 
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words" 
) 
# format prompt 
formatted_prompt = prompt.format(
    topic = "Transformers" 
) 
print(formatted_prompt) 