
### Examples on Using `while` Loops

Here are some examples to illustrate how `while` loops are used in Python:

**Example 1: Basic While Loop**

Print numbers from 1 to 5 using a `while` loop.

```python
i = 1
while i <= 5:
    print(i)
    i += 1

```

Output:

```
Copy code
1
2
3
4
5

```

**Example 2: Sum of Numbers**

Calculate the sum of numbers from 1 to 10 using a `while` loop.

```python
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print(total)  # Output: 55

```

**Example 3: Infinite Loop with Break**

Create an infinite loop that breaks when a condition is met.

```python
i = 0
while True:
    print(i)
    i += 1
    if i == 5:
        break

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

**Example 4: While Loop with Continue**

Skip the number 3 while printing numbers from 1 to 5 using `continue`.

```python
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

```

Output:

```
Copy code
1
2
4
5

```

**Example 5: User Input**

Keep asking the user for a password until the correct one is entered.

```python
password = "secret"
user_input = ""

while user_input != password:
    user_input = input("Enter the password: ")
print("Access granted.")

```

Output (example session):

```mathematica
mathematicaCopy code
Enter the password: hello
Enter the password: secret
Access granted.

```

**Example 6: Counting Down**

Count down from 10 to 1 and print "Happy New Year!".

```python
i = 10
while i > 0:
    print(i)
    i -= 1
print("Happy New Year!")

```

Output:

```sql
sqlCopy code
10
9
8
7
6
5
4
3
2
1
Happy New Year!

```

**Example 7: Collatz Conjecture**

Apply the Collatz Conjecture to a number: if it's even, divide it by 2; if it's odd, multiply by 3 and add 1, until it reaches 1.

```python
n = 6
while n != 1:
    print(n)
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
print(n)

```

Output:

```
Copy code
6
3
10
5
16
8
4
2
1

```

**Example 8: Sum of Digits**

Calculate the sum of digits of a number using a `while` loop.

```python
number = 1234
total = 0
while number > 0:
    digit = number % 10
    total += digit
    number = number // 10
print(total)  # Output: 10

```

**Example 9: Finding the Largest Number**

Find the largest number in a list using a `while` loop.

```python
numbers = [3, 5, 2, 8, 1]
i = 1
max_number = numbers[0]

while i < len(numbers):
    if numbers[i] > max_number:
        max_number = numbers[i]
    i += 1
print(max_number)  # Output: 8

```

**Example 10: Printing List Elements**

Print each element of a list using a `while` loop.

```python
fruits = ["apple", "banana", "cherry"]
i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1

```

Output:

```
Copy code
apple
banana
cherry

```

These examples demonstrate various ways to use `while` loops in Python, including basic counting, summing, handling user input, and more complex operations like the Collatz Conjecture and list processing.