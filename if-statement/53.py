# Exercise 53: Assessing Employees

'''
Write a program that reads a rating from the user
and indicates whether the performance was unacceptable, acceptable or meritorious.
The amount of the employee’s raise should also be reported.
Your program should display an appropriate error message
if an invalid rating is entered.
'''

rate = float(input("Input the rate: "))
perfomance = {0.0:"Unacceptable", 0.4:"Acceptable", 0.6:"Meritorious"}
if 0.6 < rate:
  rate = 0.6

raised_salary = 2400 * rate
print(f"Your perfomance was {perfomance[rate]}, your salary raised to {raised_salary}")
