from pypdf import PdfReader

# Load PDF
reader = PdfReader("sample.pdf")

# Total pages
print("Total Pages:", len(reader.pages))

# Read all pages
for i, page in enumerate(reader.pages):
    text = page.extract_text()

    print(f"\n--- Page {i+1} ---")
    print(text)  