# Exercise 66: Compute a Grade Point Average

total, count = 0, 0
while True:
  letter = input("Input your Grade letter: ").upper()
  grade_points = {'A+':4.0,'A':4.0,'A-':3.7,'B+':3.3,'B':3.0,'B-':2.7,'C+':2.3,'C-':2.0,'C-':1.7,'D+':1.3,'D':1.0,'F':0}
  if letter != "":
    total += grade_points[letter]
    count += 1
  else:
    print(f"The average is {total/count}")
    break