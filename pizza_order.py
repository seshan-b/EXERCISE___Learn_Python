### Pseudo Code ###
# Print a welcome message for Python Pizza Deliveries.
# Get user input for the size of the pizza (S, M, or L).
# Get user input for whether they want pepperoni (Y or N).
# Get user input for whether they want extra cheese (Y or N).
# Initialize the bill to 0.
# If the size is 'S', add $15 to the bill.
# If the size is 'M', add $20 to the bill.
# If the size is 'L', add $25 to the bill.
# If the user wants pepperoni and the size is 'S', add $2 to the bill.
# If the user wants pepperoni and the size is 'M' or 'L', add $3 to the bill.
# If the user wants extra cheese, add $1 to the bill.
# Print the final bill.

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Initialize the bill to 0
bill = 0

# Add the base price of the pizza based on the size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else: 
    bill += 25

# Add the price of pepperoni based on the size and user choice
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Add the price for extra cheese if the user wants it
if extra_cheese == "Y":
    bill += 1

# Print the final bill
print(f"Your final bill is ${bill}")
