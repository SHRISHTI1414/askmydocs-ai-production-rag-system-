import chromadb

client = chromadb.Client()

try:
    client.delete_collection("rag_collection")
except:
    pass

collection = client.get_or_create_collection(
    name="rag_collection"
)

def store_embeddings(chunks, embeddings):

    documents = [chunk["text"] for chunk in chunks]

    ids = [str(chunk["chunk_id"]) for chunk in chunks]

    metadatas = [
        {
            "page": chunk["page"]
        }
        for chunk in chunks
    ]

    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=ids,
        metadatas=metadatas
    )