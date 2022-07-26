

# Get inputs
input_height = input("enter your height in m: ")
input_weight = input("enter your weight in kg: ")


# Assign variable and type cast
height = float(input_height) 
weight = int(input_weight)

# Calculate
bmi = weight / height ** 2


# Print
print(f" Your BMI is {str(round(bmi))}")