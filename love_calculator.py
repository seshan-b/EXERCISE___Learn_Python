print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine_string = name1 + name2

lowercase_combined_string = combine_string.lower()

t = lowercase_combined_string.count("t")
r = lowercase_combined_string.count("r")
u = lowercase_combined_string.count("u")
e = lowercase_combined_string.count("e")

true = t + r + u + e

l = lowercase_combined_string.count("l")