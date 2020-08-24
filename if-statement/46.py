month = input("Input the month : ").lower()
date = int(input("Input the date : "))

spring = ["january", "february", "march"]
summer = ["april","may","jun"]
fall = ["july","august","september"]
winter = ["october","november","december"]

if month in spring:
  if month == spring[-1] and date <= 20:
    print(f"{month}-{date} is spring")
  else:
    print(f"{month}-{date} is summer")
elif month in summer:
  if month == summer[-1] and date <= 21:
    print(f"{month}-{date} is summer")
  else:
    print(f"{month}-{date} is fall")
elif month in fall:
  if month == fall[-1] and date <= 22:
    print(f"{month}-{date} is fall")
  else:
    print(f"{month}-{date} is winter")
elif month in winter:
  if month == winter[-1] and date <= 21:
    print(f"{month}-{date} is winter")
  else:
    print(f"{month}-{date} is spring")