
# Tip calculator 

# Each person should pay ($150 / 5) * 1.12


# Round the result to 2 decimals 


# Print heading
print("Print Calculator")

# Get user input. We can also cast user input to int or float
bill = float(input("What was the total bill? $"))
tip = int(input("How much would you like to tip 10, 12, 15? "))
people = int(input("How many people would you split it with"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

bill_per_person = total_bill / people

final_amount = round(bill_per_person)

final_amount = "{:.2f}".format(bill_per_person)

print(f"Your bill is ${final_amount}")