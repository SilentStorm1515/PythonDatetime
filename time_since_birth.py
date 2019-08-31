import time
from datetime import date
date_of_birth = date(2006, 4, 23)
todays_date = date(2019, 8, 30)
days_elapsed = todays_date - date_of_birth
hours = days_elapsed * 24
minutes = hours * 60
seconds = minutes * 60

print("days:", days_elapsed)
print("hours:", hours)
print("minutes:", minutes)
print("seconds:", seconds)


