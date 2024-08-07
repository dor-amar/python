# Math Functions

### Summary and Examples of Math Functions

### **Class Summary: Math Functions**

In this class, we explored **math functions** in Python, particularly those available in the `math` module. These functions help perform a wide range of mathematical calculations, including basic arithmetic, trigonometry, and more advanced operations. Key functions include `sqrt()` for square roots, `pow()` for exponentiation, `abs()` for absolute values, and trigonometric functions like `sin()`, `cos()`, and `tan()`.

### **Examples**

**Example 1: Calculating the Square Root**

To calculate the square root of a number, you can use the `math.sqrt()` function.

```python
import math

# Calculate the square root of 25
result = math.sqrt(25)
print(result)  # Output: 5.0

```

**Example 2: Using Exponentiation**

The `math.pow()` function allows you to raise a number to a specified power.

```python
import math

# Calculate 2 raised to the power of 3
result = math.pow(2, 3)
print(result)  # Output: 8.0

```

**Example 3: Finding the Ceiling and Floor**

The `math.ceil()` function rounds a number up to the nearest integer, while `math.floor()` rounds it down.

```python
import math

# Rounding examples
number = 4.7
ceil_result = math.ceil(number)
floor_result = math.floor(number)

print(ceil_result)  # Output: 5
print(floor_result) # Output: 4

```

**Example 4: Calculating the Absolute Value**

To find the absolute value of a number, use the `abs()` function.

```python
import math

# Absolute value
negative_number = -10
absolute_value = abs(negative_number)
print(absolute_value)  # Output: 10

```

**Example 5: Trigonometric Functions**

To calculate the sine, cosine, or tangent of an angle (in radians), you can use `math.sin()`, `math.cos()`, and `math.tan()` respectively.

```python
import math

# Calculate sine, cosine, and tangent of 90 degrees
# Note: math functions take radians, so we convert degrees to radians first
degrees = 90
radians = math.radians(degrees)

sin_value = math.sin(radians)
cos_value = math.cos(radians)
tan_value = math.tan(radians)

print(sin_value)  # Output: 1.0
print(cos_value)  # Output: 6.123233995736766e-17 (close to 0)
print(tan_value)  # Output: 1.633123935319537e+16 (very large number, essentially infinity)

```

These examples demonstrate how to use some of the fundamental math functions in Python. Now, let's proceed with the exercises.