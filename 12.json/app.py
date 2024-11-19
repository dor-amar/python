import json 

# # HTTP Request to API 
# json_data = '{"name": "Dor", "age": 28, "skills": ["Python", "DevOps", "Kubernetes"]}'

# parsed_data = json.loads(json_data)
# print(type(parsed_data))

# print(parsed_data["name"])
# print(parsed_data["skills"])

python_dictionary = {
    "name" : "Dor",
    "age": 27,
    "is_student": True
}

json_data = json.dumps(python_dictionary)
print(type(json_data))
print(json_data)