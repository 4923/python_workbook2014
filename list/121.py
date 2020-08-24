# Exercise 121: Count the Elements

'''
(* 해결됨 – 49 줄 *)

Python의 표준 라이브러리에는 목록에서 특정 값이 몇 번 나타나는지 결정하는 'count'라는 메소드가 있습니다. 
이 연습에서는리스트에서 최소값 이상이고 최대 값보다 작은 요소 수를 결정하고 반환하는 'countRange라는 새 함수를 작성합니다. 
함수는 목록, 최소값 및 최대 값의 세 가지 매개 변수를 사용합니다. 0보다 크거나 같은 정수 결과를 리턴합니다.
여러 다른 목록, 최소값 및 최대 값에 대한 함수를 보여주는 기본 프로그램을 포함 시키십시오. 
정수 목록과 부동 소수점 숫자 목록 모두에서 프로그램이 올바르게 작동하는지 확인하십시오.
'''

'''
# 1. [def] countRange( list, min, max ):
# 2. return val >= 0
# 3. [def] main():
# 4. 다른 목록, 최소 및 최대값에 대한 함수?
# 5. int 부터 float 까지

?? demonstrates your function for several different lists, minimum values and maximum values
: 여러 다른 리스트 뭐 어쩌라고 반복문으로 함수 여러번 호출하란건지?
'''
 # 1 0 5 1 4 8 3 0 103  4 5 41 103 103 0 0 103

# use [count] method
# as a [return] val: the number of values which is bigger than `min` and smaller than `max`
def countRange(_list, _min, _max):  # parameter type: list, float, float
  num_min, num_max= _list.count(_min), _list.count(_max)
  # rangeList = 최대, 최소값 지운 list
  rangeList = sorted(_list)[num_min:-num_max]
  return len(rangeList) # return type: int > 0

def main():

  while True:
    # [INPUT] str in list
    _list =  list(input('\nInput your list: ').split())
    print('Press the enter to stop the program.\n')

    # condition check
    # [break] no input
    if _list == []:
      break
    # [Error] if input is alphabets
    elif [x.isalpha() for x in _list] == True:
      result = print('Wrong input. Inputs should be numbers.')

    _min, _max = min(_list), max(_list)
    _len = countRange(_list, _min, _max)
    # [convert] str to float type
    _list = [float(e) for e in _list]

    # [OUTPUT] str type
    if _len > 1:
      result = print('The number of elements between min to max vals are',_len)
    else:
      result = print('There are no values between min to max val')
  return result

if __name__ == '__main__':
  main()