"""
retriever.py — Passo 3
-----------------------
Vetoriza o documento hipotético e busca os Top-10 no índice HNSW.
"""

import faiss
import numpy as np


def retrieve_top_k(hypothetical_doc: str, model, index, documents: list[str], k: int = 10):
    print(f"[Passo 3] Buscando Top-{k} documentos no índice HNSW...")

    vec = model.encode([hypothetical_doc], convert_to_numpy=True).astype(np.float32)
    faiss.normalize_L2(vec)

    distances, indices = index.search(vec, k)

    results = []
    for dist, idx in zip(distances[0], indices[0]):
        if idx == -1:
            continue
        results.append({
            "doc_id": int(idx),
            "score_biencoder": float(1.0 - dist / 2.0),
            "text": documents[idx],
        })

    print(f"[Passo 3] Top-{k} recuperados:")
    for i, r in enumerate(results, 1):
        print(f"  [{i:2d}] score={r['score_biencoder']:.4f} | {r['text'][:80]}...")

    return results
