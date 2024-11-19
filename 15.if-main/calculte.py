import json

# Python dictionary
python_dict = {
    "name": "John",
    "age": 30,
    "is_student": False
}

# Write JSON data to a file
with open('data.json', 'w') as file:
    json.dump(python_dict, file)

