#/*
# Your Birthday var
# function to check birthday
# */
from datetime import datetime

yourBirthday = '05/01/2000'
today = datetime.today().strftime('%m/%d/%y')

def BirthdayCheck(d):
    return today == d

if BirthdayCheck(yourBirthday):
    print("🎂 Happy birthday")
else:
    print(f"Today is {today} which is not my birthday")