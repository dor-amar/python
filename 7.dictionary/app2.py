# square = []
# for i in range(1,101):
#     square.append(i ** 2)
# print(square)

# square2 = [ x**2 for x in range(1,101)]
# print(square2)





fruits = ["banana","apple","kiwi"]

## Normal print
# for fruit in fruits:
#     print(fruit)

# [print(fruit) for fruit in fruits]

# upper_fruit = []
# for fruit in fruits: 
#     upper_fruit.append(fruit.upper())
# print(upper_fruit)

fruits = [fruit.upper() for fruit in fruits ]
print(fruits)