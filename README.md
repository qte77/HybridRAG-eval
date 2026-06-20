# <project_name>

<project_description>

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

- `uv install`

1. **Run the Application**:

- **CLI Mode**: `uv run app/main.py --cli`

## Usage

- **CLI**: Use the CLI to query models directly from the command line.

## Testing

Run tests using: `pytest tests/`

## Documentation

- **Project DSL**: See [docs/project_dsl.txt](docs/project_dsl.txt) for a high-level overview of the project structure and functionality.
- **PRD**: See [docs/PRD.md](docs/PRD.md) for detailed product requirements.

## Project Structure

```sh
/
├─ app/
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
