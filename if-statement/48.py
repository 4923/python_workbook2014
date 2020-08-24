# Exercise 48: Chinese Zodiac

'''
Write a program that reads a year from the user
and displays the animal associated with that year.
Your program should work correctly for any year greater than or equal to zero,
not just the ones listed in the table.
'''

# input: a year (input(), str)
# output: animal associated with that year
# condition: not only the year listed in the table 
# but any year greater than or equal to zero should be work (1999~2012)

# convert str input to int val
year = int(input("Input a year: "))

# use if statement
if year < 0:
  print("Worng Input. Try again")
else:
  # Use general condition
  animals = {0:"Monkey", 1:"Rooster", 2:"Dog", 3:"Pig", 4:"Rat", 5:"Ox", 6:"Tiger", 7:"Hare", 8:"Dragon", 9:"Snake", 10:"Horse", 11:"Sheep"}
  print(f"The animal of the year {year} is {animals[year % 12]}")

