# Summary and Examples on Working with Lists

### **Class Summary: Working with Lists**

In this class, we learned about **lists** in Python, which are used to store multiple items in a single variable. Lists can hold items of different data types, including integers, floats, and strings. We covered how to create lists, access and modify list elements using indexing, and perform common operations like appending, inserting, and removing items. We also discussed slicing, iterating through lists, checking for the existence of elements, finding the length of lists, and using list comprehensions.

### **Examples**

**Example 1: Creating and Printing a List**

To create a list, we use square brackets `[]` and separate items with commas.

```python
# Creating a list of ages
ages = [19, 26, 23]

# Printing the list
print(ages)  # Output: [19, 26, 23]

```

**Example 2: Accessing List Elements**

We can access elements in a list using their index.

```python
# List of programming languages
languages = ["Python", "Swift", "C++"]

# Accessing elements by index
print(languages[0])  # Output: Python
print(languages[2])  # Output: C++

```

**Example 3: Appending and Extending Lists**

We use `append()` to add an item to the end of a list and `extend()` to add multiple items.

```python
# List of numbers
numbers = [21, 34, 54, 12]

# Appending a single item
numbers.append(32)
print(numbers)  # Output: [21, 34, 54, 12, 32]

# Extending the list with multiple items
numbers.extend([5, 10, 15])
print(numbers)  # Output: [21, 34, 54, 12, 32, 5, 10, 15]

```

**Example 4: Inserting Elements**

We can insert an element at a specific index using the `insert()` method.

```python
# List of numbers
numbers = [10, 30, 40]

# Inserting an element at index 1
numbers.insert(1, 20)
print(numbers)  # Output: [10, 20, 30, 40]

```

**Example 5: Removing Elements**

We can remove elements using the `del` statement or the `remove()` method.

```python
# List of programming languages
languages = ["Python", "Swift", "C++", "Java"]

# Using del to remove the second item
del languages[1]
print(languages)  # Output: ["Python", "C++", "Java"]

# Using remove() to delete a specific item
languages.remove("Java")
print(languages)  # Output: ["Python", "C++"]

```