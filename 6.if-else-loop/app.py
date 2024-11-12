"""
This block of code calculates the factorial
of a given number using an iterative approach.
"""
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
