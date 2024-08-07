
### **Practical Exercises**


### **Exercise 1: Print First and Last Character**

- Write a program that stores a string and prints its first and last character.

**Example**:

```python
text = "Example"
print(text[0])   # Output: E
print(text[-1])  # Output: e

```

### **Exercise 2: String Slicing**

- Ask the user for a word and print a substring containing the first three characters.

**Example**:

```python
word = input("Enter a word: ")
print(word[:3])

```

### **Exercise 3: Basic Arithmetic with User Input**

- Ask the user for two numbers and print their sum, difference, product, and quotient.

**Example**:

```python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Quotient:", num1 / num2)

```

### **Exercise 4: String Manipulation**

- Ask the user for a sentence, convert it to uppercase, and print the length of the sentence.

**Example**:

```python
sentence = input("Enter a sentence: ")
print(sentence.upper())
print("Length:", len(sentence))

```

### **Exercise 5: Replace in a String**

- Create a string that contains a sentence. Replace one word in the sentence with another word and print the new sentence.

**Example**:

```python
sentence = "I love programming."
new_sentence = sentence.replace("programming", "Python")
print(new_sentence)  # Output: I love Python.
```