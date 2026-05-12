"""
indexer.py — Passo 1
---------------------
Gera embeddings dos documentos e constrói o índice HNSW com FAISS.
"""

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
HNSW_M = 32
HNSW_EF_CONSTRUCTION = 200


def build_index(documents: list[str]):
    print(f"[Passo 1] Carregando modelo de embedding...")
    model = SentenceTransformer(MODEL_NAME)

    print(f"[Passo 1] Gerando embeddings para {len(documents)} documentos...")
    embeddings = model.encode(documents, convert_to_numpy=True).astype(np.float32)
    faiss.normalize_L2(embeddings)

    dim = embeddings.shape[1]
    index = faiss.IndexHNSWFlat(dim, HNSW_M)
    index.hnsw.efConstruction = HNSW_EF_CONSTRUCTION
    index.hnsw.efSearch = 50
    index.add(embeddings)

    print(f"[Passo 1] Índice HNSW construído com {index.ntotal} vetores (dim={dim})")
    return index, model
