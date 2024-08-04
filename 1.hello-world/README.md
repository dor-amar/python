# Data Types

### 1. **Introduction to Data Types**

- Definition: Data types define the type of data a variable can hold, such as numbers, text, etc.
- Importance: Understanding data types is fundamental to writing efficient and error-free code.

### 2. **Basic Data Types in Python**

- **Integer (`int`) מספר**
- **Float (`float`) מספר עשרוני**
- **String (`str`) מחרוזת**
- **Boolean (`bool`) בולאני**

https://www.programiz.com/python-programming/variables-datatypes

### 1. **Integer (`int`)**

- **Description**: Whole numbers, positive or negative, without a decimal point.

**Example**:

```python
age = 25
year = 2023
print("Age:", age)   # Output: Age: 25
print("Year:", year) # Output: Year: 2023
```

**Operations**:

```python
a = 10
b = 5
print(a + b)  # Addition: Output: 15
print(a - b)  # Subtraction: Output: 5
print(a * b)  # Multiplication: Output: 50
print(a / b)  # Division: Output: 2.0
print(a // b) # Floor Division: Output: 2
print(a % b)  # Modulus: Output: 0
```

### 2. **Float (`float`)**

- **Description**: Numbers with a decimal point.

**Example**:

```python
temperature = 36.6
pi = 3.14159
print("Temperature:", temperature) # Output: Temperature: 36.6
print("Pi:", pi)                   # Output: Pi: 3.14159
```

**Operations** (similar to integers, but with decimals):

```python
x = 5.5
y = 2.0
print(x + y)  # Output: 7.5
print(x - y)  # Output: 3.5
print(x * y)  # Output: 11.0
print(x / y)  # Output: 2.75
print(x // y) # Output: 2.0
print(x % y)  # Output: 1.5
```

### 3. **String (`str`)**

- **Description**: Sequence of characters, enclosed in single or double quotes.

**Example**:

```python
name = "Alice"
greeting = 'Hello'
print(name)       # Output: Alice
print(greeting)   # Output: Hello
print(greeting + ", " + name + "!") # Output: Hello, Alice!
```

**String Operations**:

```python
pythonCopy code
message = "Python is fun"
print(message.upper())     # Output: PYTHON IS FUN
print(message.lower())     # Output: python is fun
print(message.split())     # Output: ['Python', 'is', 'fun']
print(len(message))        # Output: 13

```

### 4. **Boolean (`bool`)**

- **Description**: Represents True or False.

**Example**:

```python
is_student = True
is_teacher = False
print(is_student) # Output: True
print(is_teacher) # Output: False
```

**Boolean Operations**:

```python
a = 10
b = 5
print(a > b)  # Output: True
print(a == b) # Output: False
print(a < b)  # Output: False
print(a != b) # Output: True
```