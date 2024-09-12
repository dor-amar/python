import re
string = "I have an apple."
match = re.search(r'apple', string)
print(match.group())  # Output: "apple"