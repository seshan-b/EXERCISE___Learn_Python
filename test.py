from calendar import c
from datetime import datetime,timedelta 

# adding 2 sting. When doing math make sure you wrap them in the right data types

# first_name = input("Enter 1st Name \n")
# last_name = input("Enter 2nd name: \n")

# math = int(first_name) + int(last_name)

# print(f"{math}")

print("--------------------------------------------------------")


days_in_feb = 28
print(str(days_in_feb) + " days in Feb")


# Current Date and Time
today = datetime.now()
print(f"Today's Date is: {str(today)}")

# Time Delta is used to define a period of time
one_day = timedelta(days = 1)
yesterday = today - one_day

print(f"Yesterday was {yesterday}")


# Input date
today = datetime.now()

print(f"Today {today}")

print("--------------------------------------------------------")


input_text = input("hello world")

get_text = input_text[1]

print(f"{get_text}")