# Exercise 125: Does a List contain a Sublist?

# input
user_Ori = list(map(int,input('Input a origin list: ').split()))
user_Sub = list(map(int,input('Input a sub list: ').split()))

def isSublist(origin, sub):
  sub_index = origin.index(sub[0])
  sublist = []
  for i in range(len(sub)):
    sublist.append(origin[sub_index])
    sub_index += 1
    
  if sub == sublist:
    return True
  else:
    return False

def main():
  if isSublist(user_Ori, user_Sub) == True:
    result = f'The list {user_Sub} is sublist of {user_Ori}'
  else:
    result = f'The list {user_Sub} is NOT sublist of {user_Ori}'
  return result

if __name__ == "__main__":
  print(main())
