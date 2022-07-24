

# Get input 
age_input = input("What is your current age?")

# Assign age to user input
age = age_input

# Calculate
max_age = 90 - int(age)
months = round(max_age * 12)
weeks = round(max_age * 52)
days = round(max_age * 365)

# Print and cast to string
print('You have ' + str(days) + ' days, ' + str(weeks) + ' weeks, and ' + str(months) + ' months left.')
