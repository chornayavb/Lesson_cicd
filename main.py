def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero!")
    return a / b

def is_even(n):
    return n % 2 == 0

def is_odd(n):
    return n % 2 != 0

def factorial(n):
    if n < 0:
        raise ValueError("Negative number!")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def max_of_list(lst):
    if not lst:
        raise ValueError("Empty list!")
    return max(lst)