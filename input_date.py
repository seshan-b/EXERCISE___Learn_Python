from datetime import datetime, timedelta

birthday = input ("When is your birthday (dd/mm/yyyy)? \n")

birthday_date = datetime.strptime(birthday, "%d/%m/%Y")

print(f"Birthday {str(birthday_date)}")

