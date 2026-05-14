from langchain_text_splitters import TokenTextSplitter 
text = """Artificial Intelligence is transforming industries. Machine Learning powers recommendation systems. 
          Deep Learning uses neural networks.""" 
# create token splitter 
splitter = TokenTextSplitter(
    chunk_size = 5,
    chunk_overlap= 2
) 
# split text 
chunks = splitter.split_text(text) 
# print chunks 
for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print("-" * 20)
    print(chunk) 