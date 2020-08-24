# Exercise 120: Is a List already in Sorted Order?

user_list = list(map(int,input('Input your list: ').split()))
sorted_list = sorted(user_list)

def isSorted():
  if len(user_list) > 1:
    if user_list == sorted_list:
      return True
    elif user_list == sorted_list(reverse = True):
      return True
    else:
      return False
  else:
    return -1

def main():
  if isSorted() == True:
    result = f'The list {user_list} is already sorted'
  elif isSorted() == -1:
    result = f'The list {user_list} is no neet to be sorted. The list has less than 1 element'
  else:
    result = f'The list {user_list} is needed to be sorted'
  return result

if __name__ == "__main__":
  print(main())
  

