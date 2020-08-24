# Exercise 115: Pig Latin

# 1.
# y포함 자음으로 시작하는경우 y제외 첫 모음까지
# 단어의 시작부분의 모든 글자를 제거한 후 끝에 ay 추가.
# computer -> omputer + c + ay // o 앞까지의 자음 제거 후 끝에 ay 추가
# think -> ink + th + ay // i 앞까지의 자음 제거 후  끝에 ay 추가

# 2.
# y포함 X 모음으로 시작하는경우 끝에 way 추가
# algorithm -> algorithm + way
# office -> office + way

# 입력 문자열에는 소문자와 공백만 포함된다고 가정

def changed(text, vowels):  # input str, output changed text
  # 1. 첫 문자가 모음일 때
  if text[0] in vowels:
    result = ''.join(text) + 'way'
  # 2. 모음이 하나도 없을 때, 원래 문자열 그대로 받음
  elif [x for x in list(text) if x in vowels] == None:
    result = ''.join(text)
  # 3. 첫 문자 이후에 모음이 있을 때
  else:
    # v = text의 첫 모음원소, type(v) = str
    v = [v for v in text if v in vowels][0]
    index = text.index(v) # 첫 모음의 index

    # 3-1 앞 뒤 조합 변경, type(text_result) = list
    text_front, text_back = text[:index], text[index:]  # index를 기준으로 앞 뒤 slice
    text_result = text_back + text_front

    # 4. 끝문자 ay 추가, list에서 str로 변경
    result = ''.join(text_result) + 'ay'
  return result

  
def main():
  eng = list(input('Input your message: ').strip()) # list
  vowels = ['a','e','i','o','u','y']  # list
  return changed(eng, vowels)

if __name__ == '__main__':
  print(main())
