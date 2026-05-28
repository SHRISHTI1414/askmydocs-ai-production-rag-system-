from pdf_loader import extractor
from pdf_loader import chunk_text
from embeddings import create_embeddings
from vector_store import store_embeddings
from retriever import retrieve_chunks
from generator import generate_answer

path="/Users/shrishtiyadav/Documents/rag_project/data/sample.pdf"
text=extractor(path)

chunks = chunk_text(text)


# print(text)
 

embeddings = create_embeddings(chunks)
store_embeddings(chunks, embeddings)

query = "What are Shrishti's skills?"

context = retrieve_chunks(query)

answer = generate_answer(query, context)

print("\nFINAL ANSWER:\n")
print(answer)

print("\n\nRETRIEVED CONTEXT:\n")
print(context)
 


 