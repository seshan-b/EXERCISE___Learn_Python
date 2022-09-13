from datetime import datetime, timedelta

birthday = input ("When is your birthday (dd/mm/yyyy)? \n")

birthday_date = datetime.strptime(birthday, "%d/%m/%Y")

print(f"Birthday {str(birthday_date)}")


one_day = timedelta(days = 1)
birthday_eve = birthday_date - one_day
print(f"Day before my birthday is {str(birthday_eve)}")