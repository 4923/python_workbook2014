
def age_convert_human_to_dog():
  human_ages = int(input("Input your age (unit:year) : "))
  if human_ages <= 0:
    print("Please input natural number")
  elif human_ages > 2:
    dog_ages = 10.5 + 4 * human_ages
    result = print(f"{human_ages} year is {dog_ages} year for dogs")
  else:
    dog_ages = (10.5/2) * human_ages
    result = print(f"{human_ages} year is {dog_ages} year for dogs")
    return result
age_convert_human_to_dog()

'''
(22 Lines)
It is commonly said that one human year is equivalent to 7 dog years. However this simple conversion fails to recognize that dogs reach adulthood in approximately two years. As a result, some people believe that it is better to count each of the first two human years as 10.5 dog years, and then count each additional human year as 4 dog years.
Write a program that implements the conversion from human years to dog years described in the previous paragraph. Ensure that your program works correctly for conversions of less than two human years and for conversions of two or more human years. Your program should display an **appropriate error message** if the user enters a **negative number**.
'''