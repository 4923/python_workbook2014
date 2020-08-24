# Exercise 49: Richter Scale

'''
Write a program that reads a magnitude from the user
and displays the appropriate descriptor as part of a meaningful message.
For example, if the user enters 5.5 then your program should indicate
that a magnitude 5.5 earthquake is considered to be a moderate earthquake.
'''

import math

magnitude = float(input("Input the magnitude: "))
if magnitude == 0:
  print("There is no description of magnitude 0.0")
else:
  descriptor = {1:"Micro", 2:"Very minor",3:"Minor", 4:"Light", 5:"Moderate", 6:"Strong", 7:"Major", 8:"Great", 9:"Great", 10:"Meteoric"}
  print(f"a magnitude {magnitude} earthquake is considered to be a {descriptor[math.floor(magnitude)]} earthquake.")