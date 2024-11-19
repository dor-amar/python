# lambda x : experssion 

# Example 
# add = lambda x, y : x + y 
# print(add(2,3))

# square = lambda x : x * 2 
# print(square(4))

# to_upper = lambda s : s.upper()
# print(to_upper("hello"))

# start = lambda s : s.startswith('h')
# print(start("hello"))
# print(start("Hello"))

words = ["apple","banana","cherry"]
uppercase = list(map(lambda s: s.upper(), words))
print(type(map(lambda s: s.upper(), words)))
print(uppercase)