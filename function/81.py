# Exercise 81: Compute the Hypotenuse

import math
a, b = map(int, input("Input short lengths: ").split())  # input

def cal_hypotenuse(a,b):
  return math.sqrt(math.pow(a, 2) + math.pow(b, 2))

def main():
  print( f"The hypotenuse of the triangle is {int(cal_hypotenuse(a, b))}" ) # output

main()
  