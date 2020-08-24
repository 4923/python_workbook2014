# Exercise 133: Write Out Numbers in English

'''
(*65 선*)

최근 수표의 지급방식으로 인기가 낮아졌지만, 일부 회사들은 여전히 수표를 발행하여 직원이나 판매업자에게 지불하고 있다. 
지급되는 금액은 보통 수표에 두 번 나타나는데, 한 건은 숫자로 쓰고, 다른 건 영문으로 쓴다. 
두 가지 형태로 금액을 반복하면 부도덕한 직원이나 판매업자가 수표에 적힌 금액을 입금하기 전에 수정하기가 훨씬 더 어려워진다.

이 연습에서 당신의 임무는 0에서 999 사이의 정수를 유일한 매개 변수로 삼는 함수를 만들고, 
그 숫자에 대한 영어 단어를 포함하는 문자열을 반환하는 것이다. 
예를 들어, 함수에 대한 매개변수가 142인 경우 함수는 "142"를 반환해야 한다. 
대형 if/elif/else 구성 대신 하나 이상의 사전을 사용하여 솔루션을 구현하십시오. 
사용자로부터 정수를 읽고 그 값을 영어 단어로 표시하는 메인 프로그램을 포함한다.
'''

n = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}  # 일의자리
nn = {1:'ten',2:'twenty',3:'thirty',4:'fourty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}  # 십의자리

def numb2eng(num):
  eng, status = [], True
  while status:
    if num >= 100:  # 백의자리
      eng.append('hundred')
      if num >= 200:  # 이백 이상일 때
        eng[0] = f'{n[int(num/100)]} {eng[0]}s'
      num = num%100

    elif num >= 10: # 십의자리
      eng.append(nn[int(num/10)])
      num = num%10
      
    elif num >= 1:  # 일의자리
      eng.append(n[num])
      num = num
      status = False
    else:
      break
  return ' '.join(eng)

def main():
  num = int(input('How much money do you want to issue cheques?: '))
  return f'number {num} is "{numb2eng(num).title()}" in english'

if __name__=='__main__':
  print(main())

