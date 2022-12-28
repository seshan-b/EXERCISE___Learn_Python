import math


def calculator():
    num1 = float(input("What is the first number?"))
    while True:
        input_str = input("Enter an operation and number (e.g. '* 4' to multiply by 4):")
        try:
          operation_symbol, num2_str = input_str.split()
          num2 = float(num2_str)
        except ValueError:
          print("Invalid input. Please try again.")
        continue
              if operation_symbol == "+":
            num1 += num2
                    elif operation_symbol == "-":
            num1 -= num2
                elif operation_symbol == "*":
            num1 *= num2