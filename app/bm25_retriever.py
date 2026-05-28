from rank_bm25 import BM25Okapi

bm25 = None
chunks_store = []


def setup_bm25(chunks):

    global bm25
    global chunks_store

    chunks_store = chunks

    tokenized_chunks = [
        chunk["text"].split()
        for chunk in chunks
    ]

    bm25 = BM25Okapi(tokenized_chunks)


def bm25_search(query, top_k=3):

    global bm25
    global chunks_store

    tokenized_query = query.split()

    scores = bm25.get_scores(tokenized_query)

    ranked_chunks = sorted(
        zip(chunks_store, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        chunk["text"]
        for chunk, score in ranked_chunks[:top_k]
    ]