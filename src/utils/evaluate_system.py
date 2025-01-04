from typing import Any, List, Tuple

def evaluate_system(
    database: Any, model: Any, 
    dataset: List[Tuple[str, str]]
) -> List[Tuple[float, float]]:
    results = []
    model # TODO
    for question, ground_truth in dataset:
        answer, runtime = database.query(question)
        accuracy = calculate_accuracy(answer, ground_truth)
        results.append((accuracy, runtime))
    return results

# Helper function for evaluate_system
def calculate_accuracy(
    answer: str, ground_truth: str
) -> float:
    return float(answer.lower() == ground_truth.lower())

