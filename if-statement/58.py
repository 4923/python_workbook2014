# Exercise 58: Next Day

# input
year,month,date = map(int,input("What date is today? (ex: 2013-12-01): ").split("-"))

# basic form
if month in [1,3,5,7,8,10]:
  if date == 31:
    month += 1
    date = 1
elif month in [4,6,9,11]:
  if date == 30:
    month += 1
    date = 1
elif month == 12:
  if date == 31:
    year += 1
    month = 1
    date = 1

# leap year check
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      result = 'leap year'
    else:
      result = 'not leap year'
  else:
    result = 'leap year'
else:
  result = 'not leap year'

# if leap year
if month == 2:
  if result == 'leap year':
    if date == 29:
      month += 1
      date = 1
  else:
    if date == 29:
      month += 1
      date = 1

# output
print(f"Tomorrow is {year}-{month}-{date}")