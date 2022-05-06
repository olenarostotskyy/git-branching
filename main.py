from calendar import weekday
from datetime import datetime
from time import strftime 

def good_morning(day):
  weekday=datetime.today().strftime("%A")
  print(f"Good morning? Happy {day}~")

good_morning("friday")


