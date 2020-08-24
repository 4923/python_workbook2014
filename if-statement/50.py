# Exercise 50: Roots of a Quadratic Function

'''
Write a program that computes the real roots of a quadratic function.
Your program should begin by prompting the user
for the values of a ,b and c.
Then it should display a message indicating the number of real roots,
along with the values of the real roots (if any).
'''
# output: the number of real roots, with the valus of the real roots (if any)
while True:
  a, b, c= map(int, input("Input a and b (ex:1 3 5): ").split())
  if a == 0:
    print("Wrong input. A shouldn't be 0. try again")
  else:
    # check if real roots (Rroot) are exist
    _D = b**2 - 4*a*c

    if _D > 0:
      number_Rroot = 2
      val_Rroot = (-b + (_D**1/2)) / (2*a), (-b - (_D**1/2)) / (2*a)
    elif _D == 0:
      number_Rroot = 1
      val_Rroot = -b / (2*a)
    else:
      number_Rroot = 0
      root = "imaginary number"
    
    print(f"The number of real root(s) is {number_Rroot}, and the value of root(s) is(are) {val_Rroot}")
    break