import json
import openllm
from icecream import ic

# Check the available attributes in openllm
print(dir(openllm))

# Assuming the correct class name and method
try:
    # Load a model (make sure 'base_model' is the correct model identifier)
    model = openllm.load_model('base_model')  # Use appropriate method if 'OpenLLM' doesn't exist
except AttributeError:
    print("Error: The OpenLLM class or method might be incorrect.")
    model = None

def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} contains invalid JSON.")
        return None

# Example usage
file_path = 'ygk/files/ancient-empires.json'
json_data = load_json(file_path)

if json_data:
    for item, desc in json_data.items():
        ic(item, desc)  # Print item and description
    
    # Ensure that the model is correctly loaded before generating text
    if model:
        prompt = "Once upon a time in a land far, far away"
        response = model.generate(prompt, max_length=100)  # Adjust `max_length` as needed
        print(response)
    else:
        print("Model not loaded successfully.")
else:
    print("JSON data could not be loaded.")
