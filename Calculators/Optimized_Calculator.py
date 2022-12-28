# Import the math module to provide support for computing powers
import math

def calculator():
    # Get the first number from the user
    num1 = float(input("What is the first number?"))

    # Start an infinite loop to allow the user to perform multiple calculations
    while True:
        # Get the operation and second number from the user
        input_str = input("Enter an operation and number (e.g. '* 4' to multiply by 4):")
        try:
            # Split the input string into the operation and the second number
            operation_symbol, num2_str = input_str.split()
            # Convert the second number string to a float
            num2 = float(num2_str)
        except ValueError:
            # If the input string is not in the correct format, print an error message and continue the loop
            print("Invalid input. Please try again.")
            continue

        # Use a series of if statements to determine the operation and perform the calculation
        if operation_symbol == "+":
            num1 += num2
        elif operation_symbol == "-":
            num1 -= num2
        elif operation_symbol == "*":
            # Use the *= operator to perform in-place multiplication
            num1 *= num2
        elif operation_symbol == "/":
            # Use the /= operator to perform in-place division
            num1 /= num2
        elif operation_symbol == "^":
            # Use the math.pow() function to compute powers
            num1 = math.pow(num1, num2)
        else:
            # If the operation is not recognized, print an error message and continue the loop
            print("Invalid operation. Please try again.")
            continue

        # Print the result of the calculation
        print(f"{num1} {operation_symbol} {num2} = {num1}")

        # Ask the user if they want to continue calculating with the result
        if input(f"Type 'y' to continue calculating with {num1}:") != "y":
            # If the user does not want to continue, break out of the loop
            break

# Call the calculator function to start the program
calculator()
