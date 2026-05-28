from sentence_transformers import CrossEncoder

reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

def rerank_results(query, documents, top_k=3):

    pairs = [[query, doc] for doc in documents]

    scores = reranker.predict(pairs)

    scored_docs = list(zip(documents, scores))

    ranked_docs = sorted(
        scored_docs,
        key=lambda x: x[1],
        reverse=True
    )

    top_docs = [doc for doc, score in ranked_docs[:top_k]]

    return top_docs