'''
(*Solved—21 Lines*)
In this exercise, you will create a program that reads words from the user until the user enters a blank line. After the user enters a blank line your program should display each word entered by the user exactly once. The words should be displayed in the same order that they were entered. For example, if the user enters:
'''

# Exercise 107: Avoiding Duplicates
# Preserve order (not using set)
status, vals = True, []
while status:
  val = input('Input your value: ')
  if val not in vals:
    vals.append(val)
  if val == '':
    status = False
    [print(i) for i in vals]
