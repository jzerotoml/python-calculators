def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: you can't divide for 0"
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error: you can't calculate the square root of a negative number"
    return a ** 0.5