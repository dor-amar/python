# Define Dictionary
student = {
    'name': 'Dor',
    'age': 27,
    'courses': ["Math","Computer Scince"],
    'rate': 7.8
}

# Access Values
print(student['name'])
print(student['age'])
print(student['courses'])
print(student['courses'][0])

# Access Values with Get method
print(student.get('name'))
print(student.get('phone','Not found'))

# Add Item
student['phone'] = '043254325325'
print(student.get('phone','Not found'))

#Update 
student['name'] = "Ziv"
print(student['name'])

#Update Method 
student.update({'name': "Dor",'age': 60})
print(student)

# Remove Items 
del student['age']
print(student)

name = student.pop('name')
print(name)
print(student)

last_item = student.popitem()
print(last_item)
print(student)

last_item1 = student.popitem()
print(last_item1)
print(student)

last_item2 = student.pop()
print(last_item2)


# Iterate 

print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)

for key in student:
    print(student[key])

for key,value in student.items():
    print(key,value)


# Ex
# {'h' : 1 , 'd' : 2,}
# Hello World My Name Is Dor 

def count_char(my_string):
    char_counter = {}
    for char in my_string:
        if char in char_counter:
            char_counter[char] += 1
        else: 
            char_counter[char] = 1
            # char_counter['H'] = 1
    return char_counter

my_input = "Hello"
print(count_char(my_input))