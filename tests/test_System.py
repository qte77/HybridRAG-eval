import pytest
# import yaml
from unittest.mock import Mock, patch, mock_open
from utils import load_dataset
from utils import load_model
from utils import evaluate_system

# Load model configurations from YAML file
# with open('src/config/models.yaml', 'r') as file:
#    model_configs = yaml.safe_load(file)

@pytest.fixture
def mock_config():
    return {
        "models": {
            "gpt3": {
                "type": "GPT3",
                "params": {"model_name": "text-davinci-002", "max_tokens": 100}
            },
            "llama": {
                "type": "LLaMA",
                "params": {"model_path": "/path/to/llama", "n_ctx": 2048}
            },
            "bert": {
                "type": "BERT",
                "params": {"model_name": "bert-base-uncased", "num_labels": 2}
            }
        }
    }

@pytest.fixture
def mock_yaml_load(mock_config):
    with patch('yaml.safe_load') as mock_load:
        mock_load.return_value = mock_config
        yield mock_load

def test_load_model(mock_yaml_load):
    with patch('builtins.open', mock_open()):
        models = ["gpt3", "llama", "bert"]
        expected_types = ["GPT3", "LLaMA", "BERT"]
        expected_params = [
            {"model_name": "text-davinci-002", "max_tokens": 100},
            {"model_path": "/path/to/llama", "n_ctx": 2048},
            {"model_name": "bert-base-uncased", "num_labels": 2}
        ]

        for model_name, expected_type, expected_param in \
            zip(models, expected_types, expected_params):

            model = load_model(model_name)
            assert isinstance(model, globals()[expected_type]), f"Model {model_name} should be an instance of {expected_type}"
            for param, value in expected_param.items():
                assert getattr(model, param) == value, \
                    f"Model {model_name} should have {param} set to {value}"

        with pytest.raises(
            ValueError,
            match="Model 'invalid_model' not found in configuration"
        ):
            load_model("invalid_model")

def test_load_dataset():
    dataset = load_dataset("test_dataset")
    assert isinstance(dataset, list)
    assert len(dataset) > 0
    assert all(isinstance(item, tuple) for item in dataset)
    assert all(len(item) == 2 for item in dataset)

def test_evaluate_system():
    mock_rag = Mock()
    mock_rag.query.side_effect = [
        ("Answer 1", 0.1),
        ("Answer 2", 0.2)
    ]
    test_set = [
        ("Question 1", "Ground truth 1"),
        ("Question 2", "Ground truth 2")
    ]

    results = evaluate_system(mock_rag, test_set)

    assert isinstance(results, list)
    assert len(results) == 2
    assert all(isinstance(item, tuple) for item in results)
    assert all(len(item) == 2 for item in results)
    assert all(
        isinstance(item[0], float) and isinstance(item[1], float)
        for item in results
    )

    mock_rag.query.assert_called()
    assert mock_rag.query.call_count == 2
