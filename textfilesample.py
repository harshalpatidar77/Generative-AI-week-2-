from langchain_community.document_loaders import TextLoader 
# load the text file 
loader = TextLoader("textfilesample.txt") 
# read documents 
documents = loader.load() 
# print content 
for doc in documents:
    print(doc.page_content) 