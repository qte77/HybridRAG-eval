# HybridRAG-eval

Evaluating classic RAG against HybridRAG. Test hypothesis whether added complexity and compute of HybrdiRAG is offset by better retrieval properties against classic RAG.

![Version](https://img.shields.io/badge/version-0.0.0-8A2BE2)
[![CodeFactor](https://www.codefactor.io/repository/github/qte77/HybridRAG-eval/badge)](https://www.codefactor.io/repository/github/qte77/HybridRAG-eval)
[![CodeQL](https://github.com/qte77/HybridRAG-eval/actions/workflows/codeql.yaml/badge.svg)](https://github.com/qte77/HybridRAG-eval/actions/workflows/codeql.yaml)
[![ruff](https://github.com/qte77/HybridRAG-eval/actions/workflows/ruff.yaml/badge.svg)](https://github.com/qte77/HybridRAG-eval/actions/workflows/ruff.yaml)
[![pytest](https://github.com/qte77/HybridRAG-eval/actions/workflows/pytest.yaml/badge.svg)](https://github.com/qte77/HybridRAG-eval/actions/workflows/pytest.yaml)
[![Link Checker](https://github.com/qte77/HybridRAG-eval/actions/workflows/links-fail-fast.yaml/badge.svg)](https://github.com/qte77/HybridRAG-eval/actions/workflows/links-fail-fast.yaml)
[![Deploy Docs](https://github.com/qte77/HybridRAG-eval/actions/workflows/generate-deploy-mkdocs-ghpages.yaml/badge.svg)](https://github.com/qte77/HybridRAG-eval/actions/workflows/generate-deploy-mkdocs-ghpages.yaml)
[![vscode.dev](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=vscode.dev&labelColor=2c2c32&color=007acc&logoColor=007acc)](https://vscode.dev/github/qte77/HybridRAG-eval)

## Status

(DRAFT) (WIP) ----> Not fully implemented yet

For version history have a look at the [CHANGELOG](CHANGELOG.md).

## Setup

1. **Install Dependencies**:

- `uv sync`

## Usage

- **CLI Mode**: `uv run src/main.py --cli`

## Testing

Run tests using: `pytest tests/`

## Documentation

- **Project DSL**: See [docs/project_dsl.txt](docs/project_dsl.txt) for a high-level overview of the project structure and functionality.
- **PRD**: See [docs/PRD.md](docs/PRD.md) for detailed product requirements.

### Architecture

<img src="assets/images/c4-arch.dark.png#gh-dark-mode-only" alt="C4-Arch" title="C4-Arch" width="60%" />
<img src="assets/images/c4-arch.light.png#gh-light-mode-only" alt="C4-Arch" title="C4-Arch" width="60%" />

## Project Structure

```sh
/
├─ src/
│  ├─ __init__.py
│  ├─ __main__.py
│  └─ __version__.py
├─ tests/
├─ docs/
│  ├─ project_dsl.txt
│  ├─ PRD.md
│  └─ architecture/
│     └─ c4_diagram.md
├─ Dockerfile
├─ README.md
└─ pyproject.toml
```

## TODO

0. Definitions, Differences

    - Embeddings, VectorDB, GraphDB, Knowledge Graph (KG)
    - RAG, HybridRAG, [CAG (Cache-Augmented Generation)](https://arxiv.org/abs/2412.15605)

1. Setup Vector Database(s)

   - Local: [FAISS (Meta)](https://github.com/facebookresearch/faiss), [VectorDB (Jina.ai)](https://github.com/jina-ai/vectordb/), [qdrant](https://qdrant.tech/documentation/quickstart/), [milvus](https://milvus.io/docs), [pgvector](https://github.com/pgvector/pgvector)
   - Remote: [Pinecone (API)](https://docs.pinecone.io/reference/python-sdk), [Chroma](https://docs.trychroma.com/docs/overview/introduction), Weaviate

2. Setup GraphDB

   - Local: [Neo4j](https://github.com/neo4j/neo4j), [ArangoDB](https://docs.arangodb.com/)

3. Prepare Dataset

   - Domain-specific corpus, e.g., Financial
   - Test questions with ground truth

4. Select eval metrics

   - Accuracy, e.g., Faithfulness, Answer Relevance, Context Precision, Context Recall. See [Some Perspectives on HybridRAG in an ArangoDB World (October 8 2024)](https://arangodb.com/2024/10/some-perspectives-on-hybridrag-in-an-arangodb-world/)

5. Comparison

## Pseudocode

```python
import *
class RAG:
    query()
class HybridRAG(RAG)
    init.super()
    query()
def eval(rag_system, test_set)
def load_test_set()
# get results
compare_results(rag_results, hybrid_rag_results)
```

## Further Reading

### Papers

- [Don't Do RAG: When Cache-Augmented Generation is All You Need for Knowledge Tasks | 2412](https://arxiv.org/abs/2412.15605)
- [Domain-Specific Retrieval-Augmented Generation Using Vector Stores, Knowledge Graphs, and Tensor Factorization | 2410](https://arxiv.org/abs/2410.02721)
- [HybridRAG: Integrating Knowledge Graphs and Vector Retrieval Augmented Generation for Efficient Information Extraction | 2408](https://arxiv.org/abs/2408.04948)
- [Improving Retrieval Augmented Language Model with Self-Reasonin | 2407](https://arxiv.org/pdf/2407.19813)
- [Retrieval Augmented Generation or Long-Context LLMs? A Comprehensive Study and Hybrid Approach | 2407](https://www.arxiv.org/pdf/2407.16833)
- [From Local to Global: A Graph RAG Approach to Query-Focused Summarization | 2404](https://arxiv.org/abs/2404.16130)

### Articles

- [Optimize AI Model Performance and Maintain Data Privacy with Hybrid RAG](https://developer.nvidia.com/blog/optimize-ai-model-performance-and-maintain-data-privacy-with-hybrid-rag/)
- [HybridRAG: Combining Knowledge Graphs and Vector Retrieval](https://www.sciphi.ai/blog/hybridrag)
- [Some Perspectives on HybridRAG in an ArangoDB World (October 8 2024)](https://arangodb.com/2024/10/some-perspectives-on-hybridrag-in-an-arangodb-world/)
