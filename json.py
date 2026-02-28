# json.py

import json

# 1. Convert dictionary to JSON string
def dict_to_json(data_dict):
    return json.dumps(data_dict, indent=4)


# 2. Convert JSON string to dictionary
def json_to_dict(json_string):
    return json.loads(json_string)


# 3. Save dictionary to JSON file
def save_to_file(data_dict, filename):
    with open(filename, 'w') as file:
        json.dump(data_dict, file, indent=4)


# 4. Load dictionary from JSON file
def load_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)