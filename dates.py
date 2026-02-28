# json.py

import json

# 1. Преобразовать словарь в JSON строку
def dict_to_json(data_dict):
    return json.dumps(data_dict, indent=4)


# 2. Преобразовать JSON строку в словарь
def json_to_dict(json_string):
    return json.loads(json_string)


# 3. Сохранить словарь в JSON файл
def save_to_file(data_dict, filename):
    with open(filename, 'w') as file:
        json.dump(data_dict, file, indent=4)


# 4. Загрузить словарь из JSON файла
def load_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)