from langchain_core.prompts import PromptTemplate 
template = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple words"
) 
prompt = template.format(topic="AI") 
print(prompt)    


