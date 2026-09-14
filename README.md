# python-calculators
This repository documents the evolution of my programming skills through the step-by-step development of Python calculators, from basic implementations to more advanced applications.

## Version 2

Version 2 improves the original calculator by separating the user interface from the mathematical operations.

Instead of keeping all the logic in a single file, the project now uses two modules:

* `main.py` handles the menu, user input, and program flow.
* `operations.py` contains the mathematical operations.

This structure makes the code easier to read, maintain, and extend.

## Features

The calculator currently supports:

* Addition
* Subtraction
* Multiplication
* Division
* Power
* Square root
* Input validation for invalid menu options
* Division-by-zero protection
* Negative-number protection for square roots
* Continuous operation until the user chooses to exit

## Project Structure

```text
calculator/
├── main.py
└── operations.py
```

### `main.py`

Responsible for:

* Displaying the calculator menu
* Reading user input
* Selecting the requested operation
* Displaying results
* Controlling the main program loop

### `operations.py`

Contains the mathematical functions:

* `add()`
* `subtract()`
* `multiply()`
* `divide()`
* `power()`
* `square_root()`

## Requirements

* Python 3.x

No external libraries are required.

## How to Run

Clone the repository and navigate to the calculator directory:

```bash
cd calculator
```

Run the program:

```bash
python main.py
```

## Example

```text
=== PYTHON CALCULATOR V2 ===
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Power
6. Square root
0. Exit

Select an operation: 5
Enter the first number: 2
Enter the second number: 3
Result: 8.0
```

## Version History

### V2

* Added power operation.
* Added square root operation.
* Separated mathematical operations into `operations.py`.
* Improved program organization and modularity.
* Added validation for invalid menu options.
* Added protection against division by zero.
* Added protection against calculating the square root of negative numbers.
* Added a continuous menu loop until the user exits.

### V1

The first version was created as a basic command-line calculator and served as the foundation for the current version.

## Learning Goals

This project is part of my hands-on Python learning process. Through this version, I am practicing:

* Functions
* Modules and imports
* Conditional statements
* Loops
* User input
* Basic error handling
* Code organization
* Modular programming

## Future Improvements

Possible improvements for future versions include:

* Better error handling for invalid numerical input
* More mathematical operations
* A cleaner user interface
* Unit testing
* Object-oriented programming
* Improved project architecture
* A graphical user interface (GUI)