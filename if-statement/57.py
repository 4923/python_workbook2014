# Exercise 57: Is it a Leap Year?

'''
Write a program that reads a year from the user
and displays a message indicating whether or not it is a leap year.
'''

# input
year = int(input("Input the year: "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      result = 'leap year'
    else: # 400으로 나누어떨어지지 않으므로
      result = 'not leap year'
  else: #4로 나누어떨어지지만 100으로 나누어떨어지지 않을 때
    result = 'leap year'
else: # 4로 나누어 떨어지지 않으면
  result = 'not leap year'

# output
print(f"The year {year} is {result}")