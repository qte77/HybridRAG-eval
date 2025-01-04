import argparse
from loguru import logger
from utils import (
    load_dataset, load_model, evaluate_system
)

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="HybridRAG Evaluation"
    )
    parser.add_argument(
        "--mode",
        choices=["vector", "graph", "hybrid"],
        default="vector",
        help="RAG mode to evaluate"
    )
    parser.add_argument(
        "--model",
        choices=["m1", "m2", "m3"],
        default="m1"
    )
    parser.add_argument(
        "--dataset", type=str, required=False,
        choices=["d1", "d2", "d3"],
        default="d1"
    )
    return parser.parse_args()

def load_database(mode):
    if mode == "classic":
        from src.databases import VectorRAG
        return VectorRAG()
    if mode == "classic":
        from src.databases import GraphRAG
        return GraphRAG()
    elif mode == "hybrid":
        from src.databases import HybridRAG
        return HybridRAG()
    else:
        raise ValueError(f"Invalid mode: {mode}")

def main():
    args = parse_arguments()
    logger.info(f"Starting evaluation in {args.mode} mode")

    database = load_database(args.mode)
    model = load_model(args.model)
    dataset = load_dataset(args.dataset)
    results = evaluate_system(database, model, dataset)

    logger.info("Evaluation complete")
    logger.info(f"Results: {results}")

if __name__ == "__main__":
    main()
