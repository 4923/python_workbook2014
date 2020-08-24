# Exercise 54: Wavelengths of Visible Light

'''
Write a program that reads a wavelength from the user and reports its color.
Display an appropriate error message
if the wavelength entered by the user is outside of the visible spectrum.
'''

wavelength = int(input("Input the wavelength: "))
if  380 <= wavelength <= 750:
  if 380 <= wavelength < 450:
    color = 'Violet'
  elif 450 <= wavelength < 495:
    color = 'Blue'
  elif 495 <= wavelength < 570:
    color = 'Green'
  elif 570 <= wavelength < 590:
    color = 'Yellow'
  elif 590 <= wavelength < 620:
    color = 'Orange'
  elif 620 <= wavelength <= 750:
    color = 'Red'
  print(f"Wavelength {wavelength} is the spectrum of {color}")
else:
  print("Wrong Input. enter the wavelength between 380 to 750")