import json
import os

def separate_nested_dict(data, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for key, value in data.items():
        if isinstance(value, dict):
            nested_output_dir = os.path.join(output_dir, key)
            separate_nested_dict(value, nested_output_dir)
        else:
            output_file = os.path.join(output_dir, f"{key}.json")
            with open(output_file, 'w') as json_file:
                json.dump({key: value}, json_file, indent=4)

# Read data from JSON file
with open("data/publications.json", encoding="utf-8") as file:
    data = json.load(file)

# Directory to save the separated JSON files
output_directory = "separated_json"

# Call the function
separate_nested_dict(data, output_directory)