# Exercise 64: No More Pennies
# 1 nickel = 5 pennies

sum = 0
while True:
  price = input("\nInput your price: ")
  if price == "":
    break
  else:
    sum += float(price)
    print(f"\nTotal cost is {sum}")
    if sum % 5 == 0:
      print(f"If you pay for cash,\nThe number of nikel needed to pay: {sum / 5}")
    elif sum % 5 < 2.5:
      print(f"If you pay for cash,\nThe number of nikel needed to pay: {(sum - (sum % 5)) / 5}")
