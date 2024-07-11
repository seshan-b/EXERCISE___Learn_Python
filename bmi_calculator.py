
### Pseudo Code ###
# Get user input for height in meters.
# Get user input for weight in kilograms.
# Convert the height input to a float.
# Convert the weight input to an integer.
# Calculate the BMI using the formula: BMI = weight / (height^2).
# Round the BMI to the nearest whole number.
# Print the rounded BMI.

# Get user inputs for height and weight
input_height = input("Enter your height in m: ")
input_weight = input("Enter your weight in kg: ")

# Convert the height input to a float and the weight input to an integer
height = float(input_height)
weight = int(input_weight)

# Calculate the BMI using the formula: BMI = weight / (height^2)
bmi = weight / height ** 2

# Print the rounded BMI
print(f"Your BMI is {str(round(bmi))}")
