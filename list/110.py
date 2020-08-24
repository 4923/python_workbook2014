# Exercise 110: Perfect Numbers
# 완전수 = 약수의 합이 자기 자신일 때

def isPerfect(num): # parameter int, output bool
  # comprehension으로 약수들 구하기
  divisors = [e for e in range(1,num) if num%e == 0]
  # div_sum = int, 약수의 합
  div_sum = sum(divisors)
  # 약수의 합이 자기 자신일 때 (완전수 조건을 만족할 때) bool값 return
  if div_sum == num:
    return True
  else:
    return False

def main(): # parameter X, output list
  # perfects = list, 완전수 목록
  perfects = []
  for num in range(1,10000):
    if isPerfect(num) == True:
      perfects.append(num)
  return perfects

if __name__ == "__main__":
  print(main())