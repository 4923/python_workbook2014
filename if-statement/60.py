# Exercise 60: Roulette Payouts

# generate random number
from random import randint
random = randint(1,36)
# output
print(f"\nThe spin resulted in {random}...")  
print(f"\nPay {random}")

# check color of roulette spaces
green = [0, 00]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black = [x for x in range(1,37) if not x in red ]

if random in red:
  color = 'red'
elif random in black:
  color = 'black'
elif random in green:
  color = 'green'
# output
print(f"\nPay {color}")

# output (even or odd)
if (random % 2 == 0) and (random != 0 or 00):
  print("\nPay even")
elif random % 2 == 1:
  print("\nPay odd")

# output (range of number)
if random <= 18:
  print("\nPay 1 to 18")
else:
  print("\nPay 19 to 36")




