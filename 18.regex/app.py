import re
## Basic Example
# string = "I have an apple"
# match = re.search(r'apple',string)
# print(match.group())

## 
string1 = "There are 3 apples, 4 oranges, 5 bananas"
match = re.findall(r'\d', string1)
print(match)


# Click on Edit and place your email ID to validate
email = "dor@amar@gmail.67"
valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

print("Valid email address." if valid else "Invalid email address.")