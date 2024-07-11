
### Pseudo Code ###
# Get user input for a name.
# Split the input into first name and last name.
# Assign the first part of the split input to first_name.
# Assign the second part of the split input to last_name.
# Print the first name and last name with the first letter of each capitalized.


# Get user input
user_input = input("What is your name? ")


# Get 1st and last name
first_name = user_input.split()[0]
last_name = user_input.split()[1]



# print
print(f"My name is {first_name.title()} {last_name.title()}")