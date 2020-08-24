# Exercise 63: Temperature Conversion Table
# (0°C × 9/5) + 32 = 32°F

print("{0:>10}{1:>15}".format('Celcius','Fahrenheit'))
for i in range(0,11):
  celcius = i*10
  fahrenheit = (celcius * (9/5)) + 32
  print(f"{celcius:10.2f}{fahrenheit:-15.2f}")