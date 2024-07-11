### Pseudo Code ###
# Get user input for a number.
# Convert the user input to an integer.
# Assign the integer to a variable.
# Calculate the modulus of the number by 2.
# If the result of the modulus operation is greater than or equal to 1, print "This is an odd number."
# Otherwise, print "This is an even number."

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
