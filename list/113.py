# Exercise 113: Formatting a List

'''
(* 분할 —43 줄 *)
영어로 항목 목록을 작성할 때 일반적으로 항목을 쉼표로 구분합니다.
또한 목록에 하나의 항목 만 포함되어 있지 않으면 "and"라는 단어가 일반적으로 마지막 항목 앞에 포함됩니다.
다음 네 가지 목록을 고려하십시오.

apples
apples and oranges
apples, oranges and bananas
apples, oranges, bananas and lemons

문자열 목록을 유일한 매개 변수로 사용하는 함수를 쓰십시오.
함수는 이전에 유일한 결과로 설명한 방식으로 포맷된 목록의 모든 항목을 포함하는 문자열을 반환해야 한다.
반면 예를 들어 이전에 보여 줄 뿐 리스트 4요소를 반환하거나 덜 포함하는 포함하면 당신의 기능이 정확하게 길이를 목록에 행동해야 한다. 
사용자로부터 여러 항목을 읽고, 기능을 호출하여 포맷한 다음,
기능에 의해 반환된 결과를 표시하는 메인 프로그램을 포함시킨다.
'''
# 아... 하나씩 밀리는거라고

'''
1. 입력 여러개 받음
2. 마지막 전에 and 붙임
3. 다시 시작하면 2의 목록을 and 전에 넣고
4. 추가된 항목을 and 뒤에 넣음
'''

def isFormatted(items):
  item = input('\nWhat is your item?: ')
  items.append(item)

  # [if] break condition - main func
  if item == '':
    return False

  # [if] no need to add 'and'
  if len(items) <= 1:
    return ''.join(items)

  # [else] should add 'add' before the last factor
  else:
    # [POP] the last item
    _pop = items.pop(-1)

    # [RETURN]: result that includes 'and'
    result = ', '.join(items) + ' and ' + _pop
    # [return - origin items]
    items = items.append(_pop)
    return result

def main():
  items, status = [], True
  while status:
    result = isFormatted(items)
    if result == False:
      print('--- end of program ---')
      status = result
    else:
      print(result)

if __name__ == '__main__':
  main()