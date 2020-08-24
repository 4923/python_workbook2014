b_month, b_date = map(int,input("Input your birth month and date in number : ").split())

def zodiac_check(start_mon, start_date, end_mon, end_date):
  if b_month == start_mon and start_date <= b_date:
    return True
  elif b_month == end_mon and b_date <= end_date:
    return True

if zodiac_check(12,22,1,19) == True:
  zodiac_sign = "Capricorn"

if zodiac_check(1,20,2,18) == True:
  zodiac_sign = "Aquarius"
  
if zodiac_check(2,19,3,20) == True:
  zodiac_sign = "Pisces"
  
if zodiac_check(3,21,4,19) == True:
  zodiac_sign = "Aries"
  
if zodiac_check(4,20,5,20) == True:
  zodiac_sign = "Taurus"
  
if zodiac_check(5,21,6,20) == True:
  zodiac_sign = "Gemini"
  
if zodiac_check(6,21,7,22) == True:
  zodiac_sign = "Cancer"
  
if zodiac_check(7,23,8,22) == True:
  zodiac_sign = "Leo"

if zodiac_check(8,23,9,22) == True:
  zodiac_sign = "Virgo"

if zodiac_check(9,23,10,22) == True:
  zodiac_sign = "Libra"

if zodiac_check(10,23,11,21) == True:
  zodiac_sign = "Scorpio"

if zodiac_check(11,22,12,21) == True:
  zodiac_sign = "Sagittarius"

# output
print(f"Your Zodiac sign is {zodiac_sign}")