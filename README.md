Aqui está o arquivo `README.md` atualizado e formatado, pronto para você salvar no seu projeto:


# Laboratório 09: Arquitetura RAG Avançada (HNSW, HyDE e Cross-Encoders)

Este repositório contém a entrega do Laboratório 09 do iCEV. O objetivo é implementar um pipeline de Retrieval-Augmented Generation (RAG) de nível de produção para busca semântica em manuais médicos privados, combinando indexação com HNSW, transformação de queries via HyDE e re-ranking com Cross-Encoder.

## Bibliotecas Utilizadas

* **Python 3.10+**
* **sentence-transformers** (Bi-Encoder para embeddings e Cross-Encoder para re-ranking)
* **faiss-cpu** (Banco de dados vetorial com índice HNSW)
* **transformers** (LLM local `facebook/opt-125m` para geração do Documento Hipotético — HyDE)
* **numpy** (Operações vetoriais)

## Como rodar o código

1. Clone este repositório no seu ambiente local (Ubuntu/Linux).
2. Ative o seu ambiente virtual:
```bash
source venv/bin/activate

```

3. Instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt

```

4. O processo de execução é feito em uma única etapa:
* **Pipeline completo com queries de demonstração:**
```bash
python3 pipeline.py

```


* **Pipeline com uma query customizada:**
```bash
python3 pipeline.py --query "dor no peito e falta de ar"

```





## Estrutura do Projeto

```text
lab09/
├── corpus.py       # Fragmentos de manuais médicos simulados
├── indexer.py      # Passo 1: embeddings + índice HNSW (FAISS)
├── hyde.py         # Passo 2: geração do Documento Hipotético via LLM local
├── retriever.py    # Passo 3: busca Top-10 no índice HNSW
├── reranker.py     # Passo 4: re-ranking com Cross-Encoder, retorna Top-3
├── pipeline.py     # Orquestrador: encadeia os 4 passos
└── requirements.txt

```

## O que os scripts fazem

Este projeto implementa o pipeline RAG em quatro passos fundamentais:

1. **Construção do Índice HNSW (`indexer.py`):** Carrega o modelo de embedding multilíngue `paraphrase-multilingual-MiniLM-L12-v2` e converte os fragmentos do corpus médico em vetores densos. Um índice `faiss.IndexHNSWFlat` é configurado com `M=32` e `ef_construction=200` e os vetores são adicionados a ele.
2. **Query Transformation via HyDE (`hyde.py`):** Recebe a query coloquial do usuário (ex: *"dor de cabeça latejante e luz incomodando"*) e utiliza o modelo local `facebook/opt-125m` pedindo ao LLM que gere um trecho técnico de manual médico equivalente. Esse Documento Hipotético é vetorizado e usado como âncora de busca no espaço vetorial técnico.
3. **Busca Rápida via Bi-Encoder (`retriever.py`):** O vetor do Documento Hipotético é usado numa busca ANN no índice HNSW, recuperando os **Top-10** documentos mais próximos. Os resultados com seus scores são impressos no console.
4. **Re-ranking com Cross-Encoder (`reranker.py`):** Os 10 candidatos passam pelo Cross-Encoder `ms-marco-MiniLM-L-6-v2`, que processa cada par `[query, documento]` com atenção cruzada e atribui um score de relevância mais preciso. Os documentos são reordenados e os **Top-3 finalistas** são exibidos no console, prontos para injeção no contexto do LLM gerador.

---

## Tarefa Analítica: HNSW (M e ef_construction) vs KNN Exato

Na busca KNN exata, **todos os vetores** precisam ser comparados a cada consulta — custo de memória `O(N × d)` e custo de busca `O(N)`. Com 1 milhão de documentos de dimensão 384, isso representa ~1,5 GB só de vetores.

O HNSW organiza os vetores em um **grafo hierárquico de múltiplas camadas** e navega esse grafo na busca, com custo `O(log N)`. O consumo de memória é controlado por dois hiperparâmetros:

| Hiperparâmetro | O que controla | Impacto na RAM |
| --- | --- | --- |
| **M** | Número de arestas por nó em cada camada | Dobrar M ≈ dobrar o tamanho do grafo |
| **ef_construction** | Tamanho da fila de candidatos na construção | Afeta apenas o **tempo de build**, não o índice final |

Com `M=32`, o índice HNSW para 1 milhão de documentos ocupa cerca de **370 MB** contra **1,5 GB** do KNN exato, entregando recall > 95% com latência de busca de poucos milissegundos.

---

## Nota de Crédito

Partes deste laboratório foram geradas/complementadas com IA, revisadas e validadas por Anderson Araújo do Vale.

Conforme as regras da disciplina e o contrato pedagógico sobre o uso de IA Generativa, registro que utilizei o assistente virtual para:

* Geração dos fragmentos simulados do corpus médico (`corpus.py`).
* Construção da estrutura base dos módulos do pipeline RAG.

