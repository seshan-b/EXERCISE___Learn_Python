### Pseudo Code ###
# Import the random module.
# Define lists of letters, numbers, and symbols.
# Print a welcome message.
# Get user input for the number of letters, symbols, and numbers they want in their password.
# Initialize an empty list password_list to hold the password characters.
# For each letter requested, randomly select a letter from the letters list and add it to password_list.
# For each number requested, randomly select a number from the numbers list and add it to password_list.
# For each symbol requested, randomly select a symbol from the symbols list and add it to password_list.
# Initialize an empty string generated_password.
# For each character in password_list, append it to generated_password.
# Print the generated password.


import random



# Letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


# Numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# Symbols
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

user_letters= int(input("How many letters would you like in your password?\n")) 

user_symbols = int(input(f"How many symbols would you like?\n"))

user_numbers = int(input(f"How many numbers would you like?\n"))


# Initialize list
password_list =  []


# Loop letters
for each_char in range(1, user_letters + 1):
    random_character = random.choice(letters)
    #print(random_character)
    password_list += random_character
    print(password_list)


# For numbers 
for each_char in range(1, user_numbers + 1):
    random_character = random.choice(numbers)
    #print(random_character)
    password_list += random_character
    print(password_list)
    
    
# For symbols
for each_char in range(1, user_symbols + 1):
    random_character = random.choice(symbols)
    #print(random_character)
    password_list += random_character
    print(password_list)
    
# Generate the password assign to for loop to append it and convert to string
generated_password = ""
for char in password_list:
    generated_password += char
    print(generated_password)

# Output Generated Password
print(f" Generated Password: {generated_password}")