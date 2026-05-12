"""
reranker.py — Passo 4
----------------------
Re-classifica os Top-10 candidatos com Cross-Encoder e retorna os Top-3.
"""

from sentence_transformers import CrossEncoder

MODEL_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"


def rerank(query: str, candidates: list[dict], top_n: int = 3):
    print(f"\n[Passo 4] Re-ranking com Cross-Encoder...")

    cross_encoder = CrossEncoder(MODEL_NAME)
    pairs = [(query, doc["text"]) for doc in candidates]
    scores = cross_encoder.predict(pairs).tolist()

    for doc, score in zip(candidates, scores):
        doc["score_crossencoder"] = score

    top_docs = sorted(candidates, key=lambda d: d["score_crossencoder"], reverse=True)[:top_n]

    print(f"\n[Passo 4] Top-{top_n} documentos finais:")
    print("=" * 60)
    for i, doc in enumerate(top_docs, 1):
        print(f"\n  Rank #{i}")
        print(f"  CE score : {doc['score_crossencoder']:.4f}")
        print(f"  Texto    : {doc['text'][:150]}...")
    print("=" * 60)

    return top_docs
