# Exercise 127: The Sieve of Eratosthenes

'''
(* 해결됨 —33 줄 *)

에라토스테네스의 체 (Sieve of Eratosthenes)는 2,000 년 전에
2에서 몇 사이의 소수 (100)를 쉽게 찾을 수 있도록 개발 된 기술입니다.
알고리즘에 대한 설명은 다음과 같습니다.
[새 창에서 이미지 열기] (https : / /media.springernature.com/original/springer-static/image/chp%3A10.1007%2F978-3-319-14240-1_5/MediaObjects/978-3-319-14240-1_5_Figc_HTML.gif)
! [https://media.springernature.com/lw785/springer-static/image/chp%3A10.1007%2F978-3-319-14240-1_5/MediaObjects/978-3-319-14240-1_5_Figc_HTML.gif] (https://media.springernature.com/lw785/springer-static/image/chp%3A10.1007%2F978-3-319-14240-1_5/MediaObjects/978-3-319-14240-1_5_Figc_HTML.gif)

이 알고리즘의 핵심은 한 장의 종이에서 모든 숫자를 쉽게 구분할 수 있다는 것입니다.
이것은 컴퓨터에서도 쉬운 작업입니다.

for 루프는 세 번째 매개 변수가 "범위"기능에 제공 될 때이 동작을 시뮬레이션 할 수 있습니다.
숫자가 엇갈 리면 더 이상 소수가 아니라는 것을 알지만
여전히 종이의 공간을 차지하므로 이후 소수를 계산할 때는 여전히 고려해야합니다.
결과적으로 목록에서 숫자를 제거하여 숫자를 제거하는 것을 시뮬레이션하지 않아야합니다.
대신 숫자를 replacing0으로 대체하여 숫자의 교점을 시뮬레이션 한 다음
알고리즘이 완료되면 목록의 0이 아닌 모든 값이 소수입니다.

이 알고리즘을 사용하여 2에서 사용자가 입력 한 한도 사이의 모든 소수를 표시하는 Python 프로그램을 작성하십시오.
알고리즘을 올바르게 구현하면 몇 초 안에 1,000,000 미만의 모든 소수를 표시 할 수 있습니다.

소수를 찾는이 알고리즘은 에라토스테네스의 명성만을 주장하는 것이 아닙니다.
그의 또 다른 주목할만한 성과는 지구의 둘레와 지구의 축 기울기를 계산하는 것입니다.
알렉산드리아 도서관의 사서직도 역임했다.

'''

'''
1. 왜 for의 매개변수가 세개까지 필요한가?
2. how to cross out => 수 없애지말고 0으로 대체 [replace]
3. 전체 list에서 0이 아닌 값을 return
=> 아이거 너무 한참 걸리는데...

'''

def primes(start, end, numbers):
  count = 0
  passs = 0
  m_end = end ** 0.5
  # 곱해지는 수 k
  for k in range(start, int(m_end)+1):
    # 범위 안에서의 k배수를 찾기위해 곱하는 수 v 
    for v in range(2, int((end)/k)+1):
      print('vvvvvvvvvvvvvvvvvvvvvvv',v)
      multiples = v * k
      # if numbers[multiples:].count(0) >= v*k:
      #   passs += 1
      #   print('passsssssss')
      #   continue
      # 이전에 0으로 바뀌지 않았지만 어떤 수의 배수인 경우 => 0으로 바꿈
      if multiples in numbers and numbers[numbers.index(multiples)] != 0:
        print(f'\n********************** Now in {numbers[numbers.index(multiples)]} ==> 0 , INDEX {numbers.index(multiples)} **********************\n')
        numbers[numbers.index(multiples)] = 0
        print(v,k)
        count += 1
      else:
        print(v,k)
        print(f'''========== summary ==========
        # ELSE
        # k * v = k*v == {k} * {v} = {multiples}
        # count(0) == {numbers.count(0)}

        # now in index of {[v*k]}, 
        # numbers = {numbers}
        ===================
        ''')
        count += 1
        continue
  primes = [p for p in numbers if p != 0]
  print('passsssssssssss => ', passs )
  print(count)
  return primes

def main():
  
  start = 2
  end = int(input('Input your maximum number of range to check prime number: '))
  numbers = [x for x in range(start, end+1)]  # 입력한 수 까지 검사하기 위해 end+1 로 설정
  # print('origin numbers:',numbers)
  
  return primes(start, end, numbers)

if __name__ == '__main__':
  print(main())
