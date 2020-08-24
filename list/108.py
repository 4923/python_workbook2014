# 빈 줄을 입력할 때까지 반복 (입력값: 사용자의 정수)
# 입력 종료 => 음수, 0, 양수 순으로 표기

# Your program should display each value on its own line. 에서 its own line 은 뭐 어쩌라는거지 음수 \n 0 \n 양수?

status = True
negative, zero, positive = [], [], []

while status:
  # input
  number = input("Input your number: ")
  if number == '':
    status = False
  else:
    number = int(number)
    if number < 0:
      negative.append(number)
    elif number == 0:
      zero.append(number)
    elif number > 0:
      positive.append(number)
  
# output
print(f'negative number is {negative}')
print(f'zero is {zero}')
print(f'positive number is {positive}')
