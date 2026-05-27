import chromadb

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="rag_collection"
)


def store_embeddings(chunks, embeddings):

    ids = [str(chunk["id"]) for chunk in chunks]

    documents = [chunk["text"] for chunk in chunks]

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings
    )