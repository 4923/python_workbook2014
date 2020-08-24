#Exercise 51: Letter Grade to Grade Points

'''
Write a program that begins by reading a letter grade from the user.
Then your program should compute and display the equivalent number of grade points.
Ensure that your program generates an appropriate error message
if the user enters an invalid letter grade.
'''

letter = input("Input your Grade letter: ").upper()
grade_points = {'A+':4.0,'A':4.0,'A-':3.7,'B+':3.3,'B':3.0,'B-':2.7,'C+':2.3,'C-':2.0,'C-':1.7,'D+':1.3,'D':1.0,'F':0}
if letter in grade_points:
  print(f"The grade points of grade {letter} is {grade_points[letter]}")
else:
  print("Wrong input. Enter a valid letter grade.")
