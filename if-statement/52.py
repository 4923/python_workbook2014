# Exercise 52: Grade Points to Letter Grade

'''
 In this exercise you will create a program that reverses the process
 and converts from a grade point value entered by the user to a letter grade.
 Ensure that your program handles grade point values that fall between letter grades.
 These should be rounded to the closest letter grade.
 Your program should report A+ for a 4.0 (or greater) grade point average.
'''

grade_point = float(input("Input your grade point: "))
if 4.0 <= grade_point:
  grade_letter = 'A+'
elif 3.7 <= grade_point < 4.0:
  grade_letter = 'A-'
elif 3.3 <= grade_point < 3.7:
  grade_letter = 'B+'
elif 3.0 <= grade_point < 3.3:
  grade_letter = 'B'
elif 2.7 <= grade_point < 3.0:
  grade_letter = 'B-'
elif 2.3 <= grade_point < 2.7:
  grade_letter = 'C+'
elif 2.0 <= grade_point < 2.3:
  grade_letter = 'C'
elif 1.7 <= grade_point < 2.0:
  grade_letter = 'C-'
elif 1.3 <= grade_point < 1.7:
  grade_letter = 'D+'
elif 1.0 <= grade_point < 1.3:
  grade_letter = 'D'
elif grade_point < 1.3:
  grade_letter = 'F'

print(f"Your Grade letter is {grade_letter}")