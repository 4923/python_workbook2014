
num_list = []
status = True
while status:
  number = int(input("Input a integer except 0: "))
  num_list.append(number)
  num_list.sort()
  # list에서 remove method의 return은 None
  # sort나 sorted도 마찬가지라 각각 처리해줘야한다.
  # num_list.sort().remove(0)는 안됨.
  if number == 0:
    num_list.remove(0)
    status = False
    [print(a) for a in num_list]