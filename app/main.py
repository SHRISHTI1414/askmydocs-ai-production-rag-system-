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

results = retrieve_chunks(query)

context = "\n".join(results)

answer = generate_answer(query, context)

print("\nFINAL ANSWER:\n")
print(answer)

for i, result in enumerate(results, 1):
    print(f"\nResult {i}:\n")
    print(result)

 