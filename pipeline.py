"""
pipeline.py
-----------
Orquestra os 4 passos do Lab 09.

Uso:
    python3 pipeline.py
    python3 pipeline.py --query "dor no peito e falta de ar"
"""

import argparse
from corpus import DOCUMENTS
from indexer import build_index
from hyde import generate_hypothetical_document
from retriever import retrieve_top_k
from reranker import rerank

DEMO_QUERIES = [
    "dor de cabeça latejante e luz incomodando",
    "pressão no peito irradiando pro braço com suor frio",
    "febre alta, pescoço duro e confusão mental",
]


def run(query: str, index, model):
    # Passo 2 — HyDE
    hypothetical_doc = generate_hypothetical_document(query)

    # Passo 3 — Busca HNSW
    candidates = retrieve_top_k(hypothetical_doc, model, index, DOCUMENTS)

    # Passo 4 — Re-ranking
    top_docs = rerank(query, candidates)

    return top_docs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, default=None)
    args = parser.parse_args()

    # Passo 1 — Índice (feito uma vez só)
    index, model = build_index(DOCUMENTS)

    queries = [args.query] if args.query else DEMO_QUERIES

    for q in queries:
        print(f"\n{'#' * 60}")
        print(f"  Query: \"{q}\"")
        print(f"{'#' * 60}")
        run(q, index, model)


if __name__ == "__main__":
    main()
