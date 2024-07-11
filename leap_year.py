### Pseudo Code ###
# Get user input for a year and convert it to an integer.
# Check if the year is divisible by 4.
# If true, check if the year is also divisible by 100.
# If true, check if the year is also divisible by 400.
# If true, print "Leap year".
# If false, print "Not leap year".
# If false, print "Leap year".
# If false, print "Not a leap year".


# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Check if the year is divisible by 4
if year % 4 == 0:
    # Check if the year is also divisible by 100
    if year % 100 == 0:
        # Check if the year is also divisible by 400
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
