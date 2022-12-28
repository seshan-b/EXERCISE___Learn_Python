# Define functions to perform the four basic arithmetic operations
def add(n1, n2):
    """Return the sum of n1 and n2."""
    return n1 + n2

def subtract(n1, n2):
    """Return the difference between n1 and n2."""
    return n1 - n2

def divide(n1, n2):
    """Return the quotient of n1 and n2."""
    return n1 / n2

def multiply(n1, n2):
    """Return the product of n1 and n2."""
    return n1 * n2

# Create a dictionary that maps the symbols for the four basic arithmetic operations
# to the corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}

# Define a function to perform multiple calculations
def caluclator():
    # Prompt the user for the first number
    num1 = float(input("What is the 1st Number?"))

    # Print the available operation symbols
    for symbol in operations:
        print(symbol)

    # Set a flag to indicate that the user wants to continue
    should_continue = True

    # Start a loop to allow the user to perform multiple calculations
    while should_continue:
        # Prompt the user to choose an operation
        operation_symbol = input("Pick a operation")

        # Prompt the user for the second number
        num2 = float(input("What is the next Number?"))

        # Look up the function for the chosen operation in the operations dictionary
        calculation_function = operations[operation_symbol]

        # Call the function to perform the calculation
        answer = calculation_function(num1, num2)

        # Print the result of the calculation
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Prompt the user to decide whether to continue calculating with the result
        if input(f"Type 'y' to continue calculating with {answer}:") == "y":
            # If the user wants to continue, update the first number with the result
            # and continue the loop
            num1 = answer
        else:
            # If the user does not want to continue, set the flag to False to exit the loop
            should_continue = False

            # Recursively call the calculator function to start a new calculation
            caluclator()

# Call the calculator function to start the program
caluclator()
