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