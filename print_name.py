# Get user input
user_input = input("What is your name? ")


# Get 1st and last name
first_name = user_input.split()[0]
last_name = user_input.split()[1]



# print
print(f"My name is {first_name.title()} {last_name.title()}")