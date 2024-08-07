# Export

### Logical Operators Exercises

Here are some exercises to practice using logical operators (`and`, `or`, `not`) in Python:

### **Exercise 1: Check if Number is Between Two Values**

Write a program that checks if a given number is between 10 and 20 (inclusive).

**Example**:

```python
number = 15
if 10 <= number <= 20:
    print("The number is between 10 and 20.")
else:
    print("The number is not between 10 and 20.")

```

### **Exercise 2: Check Multiple Conditions with `and`**

Write a program that checks if a given number is positive and even.

**Example**:

```python
number = 12
if number > 0 and number % 2 == 0:
    print("The number is positive and even.")
else:
    print("The number is either negative or odd.")

```

### **Exercise 3: Check Multiple Conditions with `or`**

Write a program that checks if a person is either a teenager (13-19 years old) or a senior citizen (65 years or older).

**Example**:

```python
age = 70
if (13 <= age <= 19) or (age >= 65):
    print("The person is either a teenager or a senior citizen.")
else:
    print("The person is neither a teenager nor a senior citizen.")

```

### **Exercise 4: Invert a Condition with `not`**

Write a program that checks if a string is not empty.

**Example**:

```python
text = "Hello"
if not text == "":
    print("The string is not empty.")
else:
    print("The string is empty.")

```

### **Exercise 5: Check if a List is Not Empty**

Write a program that checks if a given list is not empty.

**Example**:

```python
my_list = [1, 2, 3]
if my_list:
    print("The list is not empty.")
else:
    print("The list is empty.")

```

### **Exercise 6: Check if Number is Outside a Range**

Write a program that checks if a number is outside the range of 1 to 100.

**Example**:

```python
number = 150
if not (1 <= number <= 100):
    print("The number is outside the range of 1 to 100.")
else:
    print("The number is within the range of 1 to 100.")

```

### **Exercise 7: Check if Character is a Vowel**

Write a program that checks if a given character is a vowel.

**Example**:

```python
char = 'e'
vowels = 'aeiou'
if char in vowels:
    print(f"{char} is a vowel.")
else:
    print(f"{char} is not a vowel.")

```

### **Exercise 8: Check Login Credentials**

Write a program that checks if a username and password match predefined values.

**Example**:

```python
username = "admin"
password = "12345"
if username == "admin" and password == "12345":
    print("Login successful.")
else:
    print("Login failed.")

```

### **Exercise 9: Check if Number is Even or Divisible by 5**

Write a program that checks if a number is either even or divisible by 5.

**Example**:

```python
number = 20
if number % 2 == 0 or number % 5 == 0:
    print("The number is either even or divisible by 5.")
else:
    print("The number is neither even nor divisible by 5.")

```

### **Exercise 10: Check if String Contains Specific Characters**

Write a program that checks if a string contains both 'a' and 'b'.

**Example**:

```python
text = "alphabet"
if 'a' in text and 'b' in text:
    print("The string contains both 'a' and 'b'.")
else:
    print("The string does not contain both 'a' and 'b'.")

```

### **Exercise 11: Validate Email Address**

Write a program that checks if an email address contains both "@" and ".".

**Example**:

```python
email = "example@example.com"
if "@" in email and "." in email:
    print("The email address is valid.")
else:
    print("The email address is invalid.")

```

### **Exercise 12: Check if Year is a Leap Year**

Write a program that checks if a year is a leap year.

**Example**:

```python
year = 2020
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")

```

### **Exercise 13: Check if Password is Strong**

Write a program that checks if a password is strong. A strong password must be at least 8 characters long and contain both letters and numbers.

**Example**:

```python
password = "Pass1234"
if len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
    print("The password is strong.")
else:
    print("The password is weak.")

```

### **Exercise 14: Check if All Elements are Positive**

Write a program that checks if all elements in a list are positive numbers.

**Example**:

```python
numbers = [1, 2, 3, 4, 5]
if all(num > 0 for num in numbers):
    print("All elements are positive.")
else:
    print("Not all elements are positive.")

```

### **Exercise 15: Check if Any Element is Negative**

Write a program that checks if any element in a list is a negative number.

**Example**:

```python
numbers = [1, -2, 3, 4, 5]
if any(num < 0 for num in numbers):
    print("There is a negative element in the list.")
else:
    print("There are no negative elements in the list.")

```
