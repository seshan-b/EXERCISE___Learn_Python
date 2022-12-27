# Calculator


# Add

def add(n1, n2):
    return n1 + n2

# Subtract


def subtract(n1, n2):
    return n1 - n2

# Divide


def divide(n1, n2):
    return n1 / n2

# Multiply


def multiply(n1, n2):
    return n1 * n2


# Dictionary
operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}


# Calculate function
def caluclator():

    # Ask User
    num1 = float(input("What is the 1st Number?"))

    for symbol in operations:
        print(symbol)
    should_continue = True



   while should_continue:
        operation_symbol = input("Pick a operation")
        num2 = float(input("What is the next Number?"))
         # Calculate
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}:") == "y":
           num1 = answer
        else:
          should_continue = False
     
     

# Call it
caluclator()