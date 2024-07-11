### Pseudo Code ###
# Print a welcome message for the Love Calculator.
# Get the first name from the user.
# Get the second name from the user.
# Combine the two names into a single string.
# Convert the combined string to lowercase.
# Count the occurrences of the letters 't', 'r', 'u', and 'e' in the lowercase combined string.
# Sum the counts of 't', 'r', 'u', and 'e' to get the value of true.
# Count the occurrences of the letters 'l', 'o', 'v', and 'e' in the lowercase combined string.
# Sum the counts of 'l', 'o', 'v', and 'e' to get the value of love.
# Concatenate the values of true and love as strings, then convert the result to an integer to get the love_score.
# If the love_score is less than 10 or greater than 90, print a message that the couple goes together like coke and mentos.
# If the love_score is between 40 and 50 inclusive, print a message that the couple is alright together.
# Otherwise, print the love_score.


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Combine the names into a single string
combine_string = name1 + name2

# Convert the combined string to lowercase
lowercase_combined_string = combine_string.lower()

# Count occurrences of the letters 't', 'r', 'u', and 'e'
t = lowercase_combined_string.count("t")
r = lowercase_combined_string.count("r")
u = lowercase_combined_string.count("u")
e = lowercase_combined_string.count("e")
true = t + r + u + e

# Count occurrences of the letters 'l', 'o', 'v', and 'e'
l = lowercase_combined_string.count("l")
o = lowercase_combined_string.count("o")
v = lowercase_combined_string.count("v")
e = lowercase_combined_string.count("e")
love = l + o + v + e

# Concatenate the counts of 'true' and 'love' and convert to an integer
love_score = int(str(true) + str(love))

# Print the love score with appropriate messages
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
