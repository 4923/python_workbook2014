#nextPrime이라는 이름의 함수는 어떤 정수보다 큰 첫번째 소수 반환
#다음 소수가 나오긴 하는데 무한대로 나옴.....
def nextPrime(number):
	number += 1
	while True:
		if number!= 1:
			for i in range(2,number):
				if number % i ==0:
					number += 1
					
				else:

					return number
					
		elif number == 1:
			number += 1
			
	
number = int(input('자연수를 입력하세요: '))
print('이 숫자보다 큰 다음 소수는', nextPrime(number))