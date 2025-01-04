import yaml
from typing import Any

def load_model(model_name: str) -> Any:
    with open('src/config/models.yaml', 'r') as file:
        model_configs = yaml.safe_load(file)
    
    if model_name not in model_configs['models']:
        raise ValueError(f"Model '{model_name}' not found in configuration")
    
    config = model_configs['models'][model_name]
    model_type = globals()[config['type']]
    return model_type(**config['params'])
