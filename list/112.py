# Exercise 112: Below and Above Average

status = True
numbers, averages, belows, aboves = [], [], [], []
num_sum, count = 0,0

# input numbers in int type and Calculate average
while status:
  number = input("Input your number: ")
  if number == "":
    status = False
  else:
    numbers.append(int(number))
    num_sum += int(number)
    count += 1
average = num_sum/count

# classify numbers
for num in numbers:
  if num < average:
    belows.append(num)
  elif num == average:
    averages.append(num)
  elif num > average:
    aboves.append(num)

# output
print(f'The average value of numbers is {average}')
print(f'The numbers below average: {belows}')
if len(averages) != 0:
  print(f'The numbers of average: {averages}')
print(f'The numbers above average: {aboves}')
