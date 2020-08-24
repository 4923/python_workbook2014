# Exercise 88: Is it a Valid Triangle?
# https://www.acmicpc.net/board/view/32535

# input
sides = sorted(list(map(int,input("Inpput lengths of triangle: ").strip().split())))  # sorted list

def _is_triangle(side1, side2, side3):
  return side3 < side1 + side2

# output
if _is_triangle(sides[0],sides[1],sides[2]) == True:
  print(f"if length of sides are {sides[0]}, {sides[1]}, {sides[2]}, The sides can make triangle.")
else:
  print(f"if length of sides are {sides[0]}, {sides[1]}, {sides[2]}, The sides can NOT make triangle.")