# Exercise 126: Generate All Sublists of a List
# 와존나 모르겠다 리스트 개꼬이는데 내머리가 뒤진듯

def allSublist(origin):
  sublist, result = [], []
  # 길이
  for i in range(len(origin)):
    # 위치
    temp = []
    for j in range(len(origin)):
      if i+j <= len(origin):
        for l in range(len(origin)):
          print('l is ',l)
          temp.append(origin[l])
          print(temp)
      sublist.append(temp)
    result.append(sublist)
    print('\n')
  return sublist

def main():
  origin = [1,2,3]
  result = f'Sublists of origin list {origin} is {allSublist(origin)}'
  return result

if __name__ == "__main__":
  print(main())
