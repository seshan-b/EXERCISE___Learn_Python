### Pseudo Code ###
# Get user input for height in meters and convert it to a float.
# Get user input for weight in kilograms and convert it to a float.
# Calculate the BMI using the formula: BMI = weight / (height^2), and round the result.
# If BMI is less than 18.5, print that the user is underweight.
# If BMI is between 18.5 and 24.9, print that the user has a normal weight.
# If BMI is between 25 and 29.9, print that the user is slightly overweight.
# If BMI is between 30 and 34.9, print that the user is obese.
# If BMI is 35 or greater, print that the user is clinically obese.

# 🚨 Don't change the code below 👇
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Calculate the BMI and round it
bmi = round(weight / height ** 2)

# Print the BMI category based on the calculated value
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
