# input
month = int(input("Input the month in number : "))
date = int(input("Input the date : "))
# output
if month == 1 and date == 1:
  print("Jan 01 is New year's day")
elif month == 7 and date == 1:
  print("Jul 01 is Canada day")
elif month == 12 and date == 25:
  print("Dec 25 is Christmas day")
else:
  print("Your input doesn't match to fixed-holiday")
