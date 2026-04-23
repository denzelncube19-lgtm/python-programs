# Age Calculator
from datetime import date
birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_day = int(input("Enter your birth day: "))
today = date.today()
birth_date = date(birth_year, birth_month, birth_day)
age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
print(f"Your age is: {age} years")
days_lived = (today - birth_date).days
print(f"Days lived: {days_lived}")
