"""Example Python script with enhanced functionality."""

import sys

def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}! Welcome to Python_Repos."

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def main():
    """Run the main program logic."""
    if len(sys.argv) > 1:
        print(greet(sys.argv[1]))
    else:
        print(greet("User"))
        print(f"2 + 3 = {add(2, 3)}")

if __name__ == '__main__':
    main()
