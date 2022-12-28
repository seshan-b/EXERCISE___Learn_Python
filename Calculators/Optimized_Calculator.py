import math


def calculator():
    num1 = float(input("What is the first number?"))
    while True:
        input_str = input(
            "Enter an operation and number (e.g. '* 4' to multiply by 4):")
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
                elif operation_symbol == "/":
            num1 /= num2   elif operation_symbol == "^":
            num1 = math.pow(num1, num2)
                  else:
            print("Invalid operation. Please try again.")
            continue
          print(f"{num1} {operation_symbol} {num2} = {num1}")
          
          
           if input(f"Type 'y' to continue calculating with {num1}:") != "y":
            break
          
          
          calculator()