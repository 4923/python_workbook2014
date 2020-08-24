# Exercise 59: Is a License Plate Valid?

# input
plate = input("Input your license plate: ")
# isalpha can not check whether str is capital or not
capital_letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number = ['0','1','2','3','4','5','6','7','8','9']
capital_check, digit_check = 0, 0

for i in range(len(plate)):
  if plate[i] in capital_letter:
    capital_check += 1
  elif plate[i] in number:
    digit_check += 1

# output - valid check
if capital_check == 3 and digit_check == 3:  # old license plate
    print("Your lisence plate is old")
elif capital_check == 3 and digit_check == 4:  # new license plate
    print("Your lisence plate is new")
else:
  print("Your lisence plate is not valid for either style")

