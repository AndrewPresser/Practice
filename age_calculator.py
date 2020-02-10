from datetime import date
import re
today = date.today()


today_month = today.month
today_day = today.day
today_year = today.year

Name = input("what is your name? ")
AgeNumberRegex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
Age = AgeNumberRegex.search(input(f" Hello {Name}, what is your birthday (mm/dd/yyyy)? "))
month = int(Age.group(1))
day = int(Age.group(2))
year = int(Age.group(3))

disc_age = today_year-year
adjusted_age = today_year-year-1

if month > today_month:
	print(f"You are {adjusted_age} years old")
elif month < today_month:
		print(f"You are {disc_age} years old")
elif day > today_day:
		print(f"You are {adjusted_age} old")
elif day == today_day:
	print(f"today is your birthday! you just turned {adjusted_age}")
	  # -------------------------------- 
    #        \   ^__^
    #         \  (oo)\_______
    #            (__)\       )\/\
    #                ||----w |
    #                ||     ||
