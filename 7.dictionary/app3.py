people = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"},
    {"name": "David", "age": 40, "city": "San Francisco"},
]



def sort_my_dictionary(pepole_list,key):
    return sorted(pepole_list, key= lambda x:x.get(key,0))



my_key = "age"
print(sort_my_dictionary(people,my_key))

