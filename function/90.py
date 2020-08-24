# Exercise 90: Does a String Represent an Integer?

def isInteger(number): # str
  number = number.strip('-+')
  if len(number) < 1 or '.' in number:
      result = f'{number} is Not integer'
  else:
    result = f'{number} is integer'    
  return result

number = input("Input numbers: ").strip()  # input
print(isInteger(number))  # output
