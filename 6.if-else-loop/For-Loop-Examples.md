# Export

### Examples on Using `for` Loops

Here are some examples to illustrate how `for` loops are used in Python:

**Example 1: Iterating Through a List**

Loop through a list of fruits and print each fruit.

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

```

Output:

```
Copy code
apple
banana
cherry

```

**Example 2: Iterating Through a Range of Numbers**

Use a `for` loop to print numbers from 0 to 4.

```python
for i in range(5):
    print(i)

```

Output:

```
Copy code
0
1
2
3
4

```

**Example 3: Summing Numbers in a List**

Calculate the sum of all numbers in a list.

```python
numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print(total)  # Output: 15

```

**Example 4: Looping Through a String**

Loop through each character in a string and print it.

```python
text = "hello"
for char in text:
    print(char)

```

Output:

```
Copy code
h
e
l
l
o

```

**Example 5: Nested Loops**

Use nested `for` loops to print a pattern.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

```

Output:

```css
cssCopy code
i=1, j=1
i=1, j=2
i=1, j=3
i=2, j=1
i=2, j=2
i=2, j=3
i=3, j=1
i=3, j=2
i=3, j=3

```

**Example 6: Iterating Through a Dictionary**

Loop through the keys and values of a dictionary.

```python
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

```

Output:

```vbnet
vbnetCopy code
name: Alice
age: 25
city: New York

```

**Example 7: Using `enumerate`**

Use the `enumerate` function to get both the index and the value while iterating through a list.

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

```

Output:

```yaml
yamlCopy code
Index 0: apple
Index 1: banana
Index 2: cherry

```

**Example 8: List Comprehension**

Use a `for` loop in a list comprehension to create a new list with squared values.

```python
numbers = [1, 2, 3, 4, 5]
squares = [number**2 for number in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]

```

**Example 9: Breaking Out of a Loop**

Use the `break` statement to exit a loop early.

```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        break
    print(number)

```

Output:

```
Copy code
1
2

```

**Example 10: Skipping an Iteration**

Use the `continue` statement to skip the current iteration and proceed to the next one.

```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        continue
    print(number)

```

Output:

```
Copy code
1
2
4
5

```

These examples demonstrate various ways to use `for` loops in Python, from iterating through lists and strings to working with dictionaries and using control flow statements like `break` and `continue`.