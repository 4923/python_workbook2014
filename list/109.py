# Exercise 109: List of Proper Divisors

'''
(*36 Lines*)

A proper divisor of a positive integer, nn, is a positive integer less than nn which divides evenly into nn. Write a function that computes all of the proper divisors of a positive integer. The integer will be passed to the function as its only parameter. The function will return a list containing all of the proper divisors as its only result. Complete this exercise by writing a main program that demonstrates the function by reading a value from the user and displaying the list of its proper divisors. Ensure that your main program only runs when your solution has not been imported into another file.
'''

'''
(* 36 줄 *)

양의 정수 nn의 적절한 제수는 nn보다 작은 양의 정수이며 nn으로 균등하게 나눕니다. 
양의 정수로 된 모든 적절한 제수를 계산하는 함수를 작성하십시오. 
정수는 유일한 매개 변수로 함수에 전달됩니다. 
이 함수는 모든 적절한 제수를 포함하는 목록을 유일한 결과로 반환합니다. 
사용자로부터 값을 읽고 적절한 제수 목록을 표시하여 기능을 보여주는 기본 프로그램을 작성하여
이 연습을 완료하십시오. 
솔루션을 다른 파일로 가져 오지 않은 경우에만 기본 프로그램을 실행하십시오.
'''

def divisors(pNum):  # type(pNum): int, pNum >=0
  divisors = [i for i in range(1, pNum) if pNum % i == 0]
  return divisors

def main():
  pNum = int(input("Input your positive number: ")) # the only parameter of func named divisors
  return divisors(pNum)

if __name__ =='__main__':
  print(main())