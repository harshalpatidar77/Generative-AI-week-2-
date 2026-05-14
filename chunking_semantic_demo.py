from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import HuggingFaceEmbeddings

# Sample text
text = """
Artificial Intelligence is transforming industries.
Machine learning powers recommendation systems.

Cooking recipes require ingredients and timing.
Baking cakes needs temperature control.

Space science studies galaxies and black holes.
Astronauts explore outer space missions.
"""

# Load free Hugging Face embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create semantic chunker
text_splitter = SemanticChunker(embeddings)

# Generate chunks
docs = text_splitter.create_documents([text])

# Print chunks
for i, doc in enumerate(docs):
    print(f"\nChunk {i+1}")
    print("-" * 30)
    print(doc.page_content)   
