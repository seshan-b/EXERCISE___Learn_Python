
# Tip calculator 

# Each person should pay ($150 / 5) * 1.12


# Round the result to 2 decimals 


# Print heading
print("Print Calculator")

# Get user input. We can also cast user input to int or float
bill = float(input("What was the total bill? $"))
tip = int(input("How much would you like to tip 10, 12, 15? "))
people = int(input("How many people would you split it with"))

# Perform calculation 
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

# Round
bill_per_person = total_bill / people

# Format output
final_amount = round(bill_per_person)
final_amount = "{:.2f}".format(bill_per_person)


# Print
print(f"Your bill is ${final_amount}")