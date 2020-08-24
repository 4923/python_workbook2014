# Exercise 85: Convert an Integer to its Ordinal Number

def ordinal_nums(num):
  ordinal_nums = {1:'first', 2:'second', 3:'third', 4:'forth', 5:'fifth', 6:'sixth', 7:'seventh', 8:'eighth', 9:'ninth', 10:'tenth', 11:'eleventh', 12: 'twelfth'}
  return ordinal_nums[num].title()

num = int(input("Input a number to check (1~12): "))  # input: int

# output
if 1 <= num <= 12:
  print(f"The number {num} is {ordinal_nums(num)}")
else:
  print('') # error: if num is in proper range, print empty str