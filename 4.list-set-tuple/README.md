# Lists, Sets, and Tuples

### Summary and Exercises on Lists, Sets, and Tuples

### **Class Summary: Lists, Sets, and Tuples**

In this class, we covered **lists**, **sets**, and **tuples** in Python, which are all used to store collections of items.

- **Lists**: Mutable collections that can store items of different types. They allow duplicate elements and are ordered by index.
- **Sets**: Unordered collections of unique elements. Sets do not allow duplicates and are typically used for membership testing and eliminating duplicates.
- **Tuples**: Immutable collections that can store items of different types. They are ordered and allow duplicates, but once created, they cannot be modified.

**When to Use Each:**

- **Lists**: Use when you need a collection of items that may change during the program's execution. Suitable for tasks like data manipulation, appending, or removing elements.
- **Sets**: Use when you need a collection of unique items and do not care about the order. Suitable for tasks like membership testing, eliminating duplicates, and set operations.
- **Tuples**: Use when you need a collection of items that should remain constant throughout the program. Suitable for fixed data like coordinates or constants.

---
### Examples
### Example: Defining a List

```python
# Defining a list of fruits
fruits = ["apple", "banana", "cherry", "date"]
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']
Example: Defining a Set
```

```python
# Defining a set of fruits
fruits_set = {"apple", "banana", "cherry", "date"}
print(fruits_set)  # Output: {'cherry', 'banana', 'date', 'apple'}
```

```python
# Defining a tuple of fruits
fruits_tuple = ("apple", "banana", "cherry", "date")
print(fruits_tuple)  # Output: ('apple', 'banana', 'cherry', 'date')
```


### **Exercises on Sets**

**Exercise 1: Create a Set**

Create a set with four different fruits and print the set.

**Exercise 2: Add Elements to a Set**

Create a set of three numbers and add a new number to the set. Print the set.

**Exercise 3: Remove Elements from a Set**

Create a set of five numbers and remove one number using the `remove()` method. Print the set.

**Exercise 4: Check Existence in Set**

Create a set of six animals and check if 'lion' is in the set. Print the result.

**Exercise 5: Set Union**

Create two sets, each with three elements, and find their union. Print the result.

**Exercise 6: Set Intersection**

Create two sets, each with three elements, and find their intersection. Print the result.

**Exercise 7: Set Difference**

Create two sets, each with three elements, and find their difference. Print the result.

**Exercise 8: Set Length**

Create a set of five elements and print the length of the set.

**Exercise 9: Clear a Set**

Create a set of three elements and clear all elements from the set. Print the set.

**Exercise 10: Iterate Through a Set**

Create a set of three programming languages and iterate through the set, printing each language.

---

### **Exercises on Tuples**

**Exercise 1: Create a Tuple**

Create a tuple with four different fruits and print the tuple.

**Exercise 2: Access Tuple Elements**

Create a tuple with five numbers and print the first and last elements using indexing.

**Exercise 3: Tuple Slicing**

Define a tuple of 10 elements and print a slice from the 3rd to the 7th element (inclusive).

**Exercise 4: Tuple Concatenation**

Create two tuples, each with three elements, and concatenate them to form a new tuple.

**Exercise 5: Nested Tuples**

Create a tuple that contains three elements, where one of the elements is another tuple. Print the nested tuple.

**Exercise 6: Tuple Unpacking**

Create a tuple with four elements and unpack the values into four variables. Print each variable.

**Exercise 7: Check Existence in Tuple**

Create a tuple of six animals and check if 'elephant' is in the tuple. Print the result.

**Exercise 8: Tuple Length**

Create a tuple of seven days of the week and print the length of the tuple.

**Exercise 9: Iterate Through a Tuple**

Create a tuple of three programming languages and iterate through the tuple, printing each language.

**Exercise 10: Immutable Nature of Tuples**

Create a tuple with three elements and try to change the second element. Print a message explaining why this is not possible.