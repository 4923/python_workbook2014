# Exercise 67: Admission Price

total = 0
while True:
  age = input("Input the age of guest: ")
  if age == "":
    print(f"Total cost is {total:.2f}")
    break
  elif 3 <= int(age) <= 12:
    total += 14
  elif 12 < int(age) < 65:
    total += 23
  elif 65 <= int(age):
    total += 18
