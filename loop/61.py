# Exercise 61: Average

'''
In this exercise you will create a program 
that computes the average of a collection
of values entered by the user.
The user will enter 0 as a sentinel value
to indicate that no further values will be provided. 

Your program should display an appropriate error message
if the first value entered by the user is 0.

Hint: Because the 0 marks the end of the input
it should not be included in the average.
'''
# input
values = input("Input a collocation of value (input 0 to mark finish): ")
col = [int(value) for value in values.split(" ")]

if col[0] == 0:
  print("Wrong input. 0 shouldn't be placed at first")
else:
  len, sum = 0, 0  
  for e in col:
    sum += e
    if e == 0:
      break
    len += 1
  average = sum / len

# output
print(f"The average of collocation is {average}")