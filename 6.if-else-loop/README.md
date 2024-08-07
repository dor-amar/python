# Export

### **Class Summary: If, Else, and Loops**

In this class, we covered **conditional statements** and **loops** in Python, which are fundamental for controlling the flow of a program.

- **If, Else Statements**: Used to execute code based on conditions.
    - **If**: Executes a block of code if the condition is true.
    - **Else**: Executes a block of code if the condition is false.
    - **Elif**: Executes a block of code if its condition is true, and previous conditions were false.
- **Loops**: Used to execute a block of code repeatedly.
    - **For Loop**: Iterates over a sequence (like a list, tuple, or string).
    - **While Loop**: Repeats a block of code as long as a condition is true.

**If, Else Syntax**:

```python
if condition:
    # block of code if condition is true
elif another_condition:
    # block of code if another_condition is true
else:
    # block of code if none of the conditions are true

```

**For Loop Syntax**:

```python
for item in sequence:
    # block of code to be executed

```

**While Loop Syntax**:

```python
while condition:
    # block of code to be executed

```

### **Examples**

**Example 1: If, Else Statement**

```python
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

```

**Example 2: For Loop**

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

```

**Example 3: While Loop**

```python
i = 1
while i <= 5:
    print(i)
    i += 1

```

**Example 4: If, Elif, Else Statement**

```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

```

**Example 5: Nested Loops**

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

```
