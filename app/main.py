from pdf_loader import extractor
from pdf_loader import chunk_text

path="/Users/shrishtiyadav/Documents/rag_project/data/sample.pdf"
text=extractor(path)

chunks = chunk_text(text)


# print(text)
print(chunks[0])