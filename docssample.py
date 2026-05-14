from langchain_community.document_loaders import Docx2txtLoader
# Path of your DOCX file
file_path = "DeepLearning.docx"
# Create loader object
loader = Docx2txtLoader(file_path)
# Load document
documents = loader.load()
# Print document content
for doc in documents:
    print(doc.page_content) 