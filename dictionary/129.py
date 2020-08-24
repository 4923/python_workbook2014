# Exercise 129: Two Dice Simulation

'''
(* 해결됨 —42 줄 *)

이 연습에서는 두 개의 주사위 1,000 롤을 시뮬레이션합니다. 
한 쌍의 6면 주사위 굴리기를 시뮬레이트하는 함수를 작성하는 것으로 시작하십시오. 
함수는 매개 변수를 사용하지 않습니다. 
두 개의 주사위에 굴린 합계를 유일한 결과로 반환합니다.

6 개의 주사위를 1,000 번 굴리는 것을 시뮬레이션하기 위해 함수를 사용하는 메인 프로그램을 작성하십시오. 
프로그램이 실행될 때 각 총 횟수가 발생하는 횟수를 계산해야합니다. 
그런 다음이 데이터를 요약 한 표를 표시해야합니다.
각 롤의 빈도를 총 롤 수의 백분율로 표시하십시오. 
또한 프로그램에는 각 총계에 대한 확률 이론에 의해 예상되는 백분율이 표시되어야합니다. 
샘플 출력은 다음과 같습니다.

'''

import random

def roll6():  # no parameter
  a = random.randint(1,6) # 1에서 6 사이의 수 하나
  b = random.randint(1,6)
  return a+b  # int type


def main():
  num = int(input('How many time do you want to simulate?: '))
  expected_p = {2:2.78, 3:5.56, 4:8.33, 5:11.11, 6:13.89, 7:16.67, 8:13.89, 9:11.11, 10:8.33, 11:5.56, 12:2.78}
  counts = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
  for i in range(1,num+1):
    rollSum = roll6() # 각 회차의 주사위 눈 합
    counts[rollSum] += 1 # rollSum을 key로 counts의 val에 개수 추가
    # [OUTPUT]
  category = '    Total\tSimulated\tExpected\n\t\t  Percent\t Percent'
  print(category,'\n--------------------------------------------')
  for j in range(1,13):
    output = f'{j+1:8d}\t{counts[j+1]/num*100:9.2f}\t{expected_p[j+1]:9.2f}'
    print(output)

if __name__ == "__main__":
  print(main())
