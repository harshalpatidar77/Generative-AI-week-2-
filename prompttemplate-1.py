from langchain_core.prompts import PromptTemplate 
template = PromptTemplate(
    input_variables=["sample"],
    template="make a short summary of {sample}"
) 
user_input = input("enter the topic which you cannot able to understand") 
prompt = template.format(sample=user_input) 
print(prompt)  