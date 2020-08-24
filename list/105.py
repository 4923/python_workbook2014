'''
Write a program that reads integers from the user and stores them in a list. Use 0 as a sentinel value to mark the end of the input. Once all of the values have been read your program should display them (except for the 0) in reverse order, with one value appearing on each line.
'''

# Exercise 105: Reverse Order (1)
vals = list(map(int,input("Input your number: ").split()))
[print(i) for i in vals[-2::-1]]  # listname[::-1] reverse list


# Exercise 105: Reverse Order (2)
vals, status = [], True
while status:
  val = int(input("Input your Value: "))
  vals.append(val)
  if val == 0:   # sentinel val: 0, end of input
    status = False
[print(i) for i in vals[-2::-1]]