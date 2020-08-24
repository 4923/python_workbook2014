name_month = input("Please input the name of month : ").lower()
_30_days = ["april","june","september","november"]

if name_month == "february":
  print(f"{name_month} has 28 days")
elif name_month in _30_days:
  print(f"{name_month} has 30 days")
else:
  print(f"{name_month} has 31 days")

# [WORKBOOK] = Start by assuming that the number of days is 31. Then update the number of days if neccesary.