Sure! Below is an example of Python code that adheres to the PEP 8 style guide. This example includes a class definition, method definitions, a function, and proper use of comments, docstrings, and naming conventions.

```python
class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.
    """

    def __init__(self, initial_value=0):
        """
        Initialize the calculator with an optional initial value.

        :param initial_value: The starting value for calculations (default is 0).
        """
        self.value = initial_value

    def add(self, number):
        """
        Add a number to the current value.

        :param number: The number to add.
        :return: The updated value.
        """
        self.value += number
        return self.value

    def subtract(self, number):
        """
        Subtract a number from the current value.

        :param number: The number to subtract.
        :return: The updated value.
        """
        self.value -= number
        return self.value

    def multiply(self, number):
        """
        Multiply the current value by a number.

        :param number: The number to multiply by.
        :return: The updated value.
        """
        self.value *= number
        return self.value

    def divide(self, number):
        """
        Divide the current value by a number.

        :param number: The number to divide by.
        :return: The updated value.
        :raises ValueError: If the number is zero.
        """
        if number == 0:
            raise ValueError("Cannot divide by zero.")
        self.value /= number
        return self.value


def main():
    """
    Main function to demonstrate the usage of the Calculator class.
    """
    calc = Calculator()

    print("Initial value:", calc.value)
    print("Add 10:", calc.add(10))
    print("Subtract 5:", calc.subtract(5))
    print("Multiply by 3:", calc.multiply(3))
    print("Divide by 2:", calc.divide(2))

    # Catch division by zero error
    try:
        calc.divide(0)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
```

### Explanation

1. **Class and Method Definitions**:
   - The `Calculator` class contains methods for basic arithmetic operations: `add`, `subtract`, `multiply`, and `divide`.
   - Each method includes a docstring describing its purpose, parameters, and return value.

2. **Docstrings**:
   - The class has a docstring at the top, providing a brief overview of its purpose.
   - Each method has a docstring explaining the parameters and the return value.
   - The `main` function also has a docstring explaining its purpose.

3. **Naming Conventions**:
   - The class name `Calculator` uses CamelCase.
   - The method and function names use lowercase_with_underscores.

4. **Whitespace**:
   - Proper use of blank lines to separate top-level function and class definitions.
   - Consistent use of spaces around operators and after commas.

5. **Comments**:
   - Inline comments are used sparingly to explain specific pieces of code (e.g., the `try` block to catch division by zero).

6. **File Organization**:
   - The code is organized with the class definition at the top, followed by the `main` function and the script entry point (`if __name__ == "__main__":`).

This example demonstrates good practices in Python coding style, making the code easy to read, maintain, and extend.