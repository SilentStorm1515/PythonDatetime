import calendar
from datetime import datetime, date

print("When were you born?(dd/mm/yyyy)")
date_of_birth = datetime.strptime(input("--->"), "%d %m %Y ")

print("What is today's date? (dd/mm/yyyy)")
current_date = input("--->")

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

age = calculate_age(date_of_birth)

print(age)
