

# Get user input
number_input = int(input("Which number do you want to check? "))

# Assign input to variable
number = number_input


# Do calculation 
mod_number =  number % 2


# Check and output number.
if (mod_number >= 1) :
    print("This is an odd number.")
else:
    print("This is an even number.")
