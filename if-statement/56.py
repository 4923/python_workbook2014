# Exercise 56: Cell Phone Bill

'''
Write a program that reads the number of minutes and text messages 
used in a month from the user.
Display the base charge, additional minutes charge (if any),
additional text message charge (if any), the 911 fee, tax
and total bill amount.
Only display the additional minute and text message charges
if the user incurred(incur: 발생시키다) costs in these categories.
Ensure that all of the charges are displayed using 2 decimal places.
'''

# basic air time : 50min + 50 text for $15.00 a month
# additional minutes of air time : $0.25
# additional text messages cost : $0.15 each
# ---
# 911 call centers $0.44
# entire bill (including 911) is subject to 5% sales tax

# input
air_time = float(input("How minutes did you use air time this month?: "))
text_count = int (input("How many texts did you send this month?: "))

# output (using 2 decimal places.)
# output 1. base charge
# output 2. additional minutes charge (if any) ***
# output 3. additional text charge (if any) ***
# output 4. 911 fee, tax and total bil amount.

# basic charge = base charge + 911 charge
print(f"\nThe basic charge is $15.00")
print(f"+ The 911 support charge is $0.44")
charge = 15.00 + 0.44

# additional charge
if air_time - 50 > 0:
  add_air_charge = 0.25 * (air_time - 50)
  print(f"+ The additional air time charge is ${add_air_charge:.2f}")
  charge += add_air_charge
else:
  add_air_charge = 0

if text_count - 50 > 0:
  add_text_charge = 0.15 * (text_count - 50)
  print(f"+ The additional text message charge is ${add_text_charge:.2f}")
  charge += add_text_charge
else:
  add_text_charge = 0

# Total bill = charge + 5% sales tax
print(f"= Totall bill is ${charge * 1.05:.2f}")