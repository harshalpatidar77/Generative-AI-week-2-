from langchain_text_splitters import RecursiveCharacterTextSplitter  
text = """AI is transforming industries.Machine Learning is a subset of AI. Deep learning uses neural networks.""" 
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 40, 
    chunk_overlap=10 
) 
chunks = splitter.split_text(text) 
for chunk in chunks:
    print(chunk) 
    print("--------") 