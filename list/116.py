# Exercise 116: Pig Latin Improved

# 첫글자가 대문자일경우 바꾼 후에도 대문자로 유지 -> .title()
# ~단어 끝의~ 구두점 (! 등) 유지

eng = input('Input your message: ').strip() # str
words = eng.split() # list, 단어 여러개일 때 분류하기 위해 split()

vowels = ['a','e','i','o','u','y']
punctuation_mark = ['!','?','@','#','$','%','^','&','*','(',')','-','_','+','=','"',"'",';','~','`','.',',']

# isUpper(text)가 True면 main 결과값에서 .title()
def isUpper(text): # input str, output bool
  return text[0].isupper()

# 문장부호가 있으면 punc_list 없으면 빈 list
def isPunctuate(text):  # input str, output list (punc_list)
  punc_list = []
  for letter in list(text):
    if letter in punctuation_mark:
      punc_list.append(letter)
      result = punc_list
    else:
      result = punc_list
  return result

# 연습문제 115번 내용
def changed(text):  # input str, output changed text
  # 1. 첫 문자가 모음일 때
  if text[0] in vowels:
    result = ''.join(text) + 'way'
  # 2. 모음이 하나도 없을 때, 원래 문자열 그대로 받음
  elif [x for x in list(text) if x in vowels] == None:
    result = text
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
  # 1. 결과값 담을 리스트
  results = []
  # 2. loop: 인풋 값인 str(eng) 안에 있는 words 수 만큼 loop 돌아감
  # 검사하는 값은 이제부터 words[i]
  for i in range (len(words)):
    # 3-1. 대문자가 있을 때 -> 마지막에 단어별.title() 처리 해야함.
    if isUpper(words[i]) == True:
      # 3-1-2. 소문자처리한 값을 교체: changed(text.lower()), type(result) = str
      result = changed(words[i].lower())

      # 4-1. 문장부호 있을 때 -> 교체된 단어의 끝에 같은 문장부호 붙이기
      if len(isPunctuate(words[i])) != 0:
        # 4-1-2. 문장부호 꺼내기
        for e in (isPunctuate(words[i])):
          # del, remove 등은 list를 사용해야하고 index도 알아야 하기 때문에 str에서 사용 가능한 replace 사용
          result = result.replace(e,"").title()
        # 4-1-3. 문장부호 마지막에 붙이기
        result += ''.join(isPunctuate(words[i]))
        results.append(result)
      # 4-2. 문장부호 없을 때
      else:
        results.append(result.title())
    # 3-2. 대문자가 없을 때
    else:
      results.append(result)
  return results

if __name__ == "__main__":
  print(main())
