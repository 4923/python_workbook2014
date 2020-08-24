_str = input("Input alphabet that you wants to know whether vowel or consonant : ").lower()

lst_vowel = ['a','e','i','o','u']
if _str in lst_vowel:
  print(f"the letter {_str} is a vowel ")
elif _str == 'y':
  print("sometimes y is a voewl, and sometimes y is a consonant")
else:
  print("the letter {_str} is a consonant")


'''
(Solved—16 Lines)
In this exercise you will create a program that reads a letter of the alphabet from the user.
If the user enters a, e, i, o or u then your program should display a message indicating that
the entered letter is a vowel.
If the user enters y then your program should display a message indicating that
sometimes y is a vowel, and sometimes y is a consonant.
Otherwise your program should display a message indicating that the letter is a consonant.
'''