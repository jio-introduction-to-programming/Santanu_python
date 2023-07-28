Topic 1: Modules / Packages

## Research: 
- 

Modules in Python:

A module in Python is simply a file containing Python definitions and statements. These files can contain variables, functions, and classes that can be used in other Python programs. When we want to use the functionality provided by a module, we need to import it into our current Python script or module.
example - '''

# math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero.")


# main.py

import math_operations

result = math_operations.add(5, 3)
print(result)  # Output: 8

result = math_operations.divide(10, 2)
print(result)  # Output: 5.0

here we have imported 'math_operations' module

Packages in Python:

A package in Python is a collection of modules organized in a hierarchical directory structure. It is essentially a directory that contains a special file called __init__.py, which indicates that the directory is a Python package. Packages provide a way to group related modules together, making it easier to organize large codebases and avoid naming conflicts.

example - 

geometry/
    __init__.py
    shapes.py
    utils.py

# geometry/shapes.py

def rectangle_area(length, width):
    return length * width

def circle_area(radius):
    return 3.14159 * radius * radius

# geometry/utils.py

def is_positive(number):
    return number > 0

Using the Package:

To use modules from the geometry package, we first need to import the specific module using the dot notation.

# main.py

from geometry import shapes, utils

result = shapes.rectangle_area(5, 3)
print(result)  # Output: 15

result = shapes.circle_area(2)
print(result)  # Output: 12.56636

is_positive = utils.is_positive(5)
print(is_positive)  # Output: True




## Implementation: 
- Create a Python module named "math_operations.py" that contains functions for basic mathematical operations such as addition, subtraction, multiplication, and division. Import this module into another Python script and demonstrate the usage of its functions.

## Exploration: 
- Research and explore popular third-party packages available in the Python Package Index (PyPI). Choose one package that interests you and explain its purpose, functionality, and how to install and use it in your Python projects.

