# Strings, Numbers, and Indexing



This folder contains exercises and examples for the basics of Python, focusing on strings, numbers, and indexing. Each subtopic has its own markdown file with exercises that aim to reinforce the concepts taught in class.

## Structure:
1. string-exercises.md: Exercises related to working with strings, including string manipulation, concatenation, and slicing.
2. number-exercises.md: Exercises focused on working with numbers, covering basic arithmetic operations, type conversions, and number manipulation.
3. indexing.md: Exercises that cover accessing elements in sequences using indexing and slicing.
### Additional Files:
- app.py: A Python script for running and testing some of the exercises in the folder.
- Exercises.md: A combined document containing all exercises.


### **1. Introduction to Strings and Numbers**

- **Strings**: A sequence of characters enclosed in quotes.
    - Single quotes: `'Hello'`
    - Double quotes: `"World"`
- **Numbers**:
    - **Integers (`int`)**: Whole numbers, e.g., `10`, `3`.
    - **Floats (`float`)**: Numbers with a decimal point, e.g., `3.14`, `2.0`.

### **2. Working with Strings**

### **2.1 Creating Strings**

```python
greeting = "Hello, World!"
name = 'Alice'

```

### **2.2 String Concatenation**

- Combining two or more strings using the `+` operator.

```python
first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)  # Output: Alice Smith

```

### **2.3 String Multiplication**

- Repeating a string multiple times using the `` operator.

```python
echo = "Echo! " * 3
print(echo)  # Output: Echo! Echo! Echo!

```

### **2.4 Accessing Characters in a String (Indexing)**

- Access individual characters using indices. Indices start at 0.

```python
word = "Python"
print(word[0])  # Output: P
print(word[2])  # Output: t

```

### **2.5 Slicing Strings**

- Extracting a substring using `[start:end]`.

```python
text = "Hello, World!"
print(text[0:5])  # Output: Hello
print(text[7:12]) # Output: World

```

### **2.6 Common String Methods**

- **`upper()`**: Converts all characters to uppercase.
- **`lower()`**: Converts all characters to lowercase.
- **`strip()`**: Removes whitespace from the beginning and end.
- **`replace(old, new)`**: Replaces occurrences of `old` with `new`.

**Examples**:

```python
message = " Hello, World! "
print(message.upper())     # Output:  HELLO, WORLD!
print(message.lower())     # Output:  hello, world!
print(message.strip())     # Output:  Hello, World!
print(message.replace("World", "Python"))  # Output: Hello, Python!

```

### **3. Working with Numbers**

### **3.1 Basic Arithmetic Operations**

- Addition (`+`), Subtraction (``), Multiplication (``), Division (`/`), and Exponentiation (`*`).

**Examples**:

```python
a = 10
b = 3
print(a + b)  # Output: 13
print(a - b)  # Output: 7
print(a * b)  # Output: 30
print(a / b)  # Output: 3.3333333333333335
print(a ** b) # Output: 1000

```

### **3.2 Converting Between Types**

- **`int()`**: Converts a value to an integer.
- **`float()`**: Converts a value to a float.
- **`str()`**: Converts a value to a string.

**Examples**:

```python
num_str = "123"
num_int = int(num_str)
print(num_int)  # Output: 123

num_float = float(num_int)
print(num_float)  # Output: 123.0

num_to_str = str(num_float)
print(num_to_str)  # Output: "123.0"

```

### **4. Indexing and Slicing**

### **4.1 Indexing Strings**

- Access individual characters using their position.

```python
phrase = "Hello"
print(phrase[0])  # Output: H
print(phrase[4])  # Output: o

```

### **4.2 Slicing Strings**

- Extract substrings using `[start:end]`.

```python
text = "Python Programming"
print(text[0:6])   # Output: Python
print(text[7:18])  # Output: Programming

```

- Omitting start or end:

```python
print(text[:6])    # Output: Python (from start to index 5)
print(text[7:])    # Output: Programming (from index 7 to end)

```

### **4.3 Negative Indexing**

- Negative indices start from the end of the string.

```python
word = "Python"
print(word[-1])  # Output: n
print(word[-3])  # Output: h

```
