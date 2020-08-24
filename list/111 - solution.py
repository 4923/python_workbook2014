# Exercise 111: Only the Words

'''
Examples of contractions include: don’t, isn’t, and wouldn’t.
then your function should return the list
["Examples", "of","contractions","include","don’t","isn’t","and","wouldn’t"].
--------------------------------------------------------------------------------
이 연습에서는 사용자가 입력 한 문자열의 모든 단어를 식별하는 프로그램을 작성합니다.
텍스트 문자열을 유일한 매개 변수로 사용하는 함수를 작성하여 시작하십시오.
함수는 단어의 가장자리에 문장 부호가 제거 된 문자열의 단어 목록을 반환해야합니다.
제거해야하는 문장 부호에는 쉼표, 마침표, 물음표, 하이픈, 아포스트로피, 느낌표, 콜론 및 세미콜론이 포함됩니다.
수축에 사용되는 아포스트로피와 같이 단어 중간에 나타나는 문장 부호를 제거하지 마십시오. 
기능을 보여주는 기본 프로그램을 작성하십시오.
사용자로부터 문자열을 읽고 문장 부호가 제거 된 문자열의 모든 단어를 표시해야합니다.
연습 158을 완료 할 때 솔루션을이 연습으로 가져와야합니다.
결과적으로 파일을 다른 프로그램으로 가져 오지 않은 경우에만 기본 프로그램이 실행되도록해야합니다.
'''

'''
0. 띄어쓰기 단위로 입력문장.split()
1. split()된 단어(type list)를 검사하여 특수문자 index 추출 할 것 (for문)
2. 특수문자 앞뒤.isalpha() == True 이면 지우지 말 것
3. 2가 아니면 지울 것
'''


'''

## SOLUTION (with prints)

# [INPUT]
# sentence = input("Input your sentence: ").strip().split()
_remove = [',','.','?','-',"’",'"','!',';',':']

def onlyTheWords(sentence):
  # [CHECK] spread elements, word in list named sentence
  for word in sentence:  # i: <class 'str'>
    print('*****************************************')
    print('\n[WORD]', word,'\n')
    print('*****************************************')
    _index = sentence.index(word)
    print('[INDEX IS] ',  _index)
    for j in range(len(word)):
      print(len(word))
      # [IF] if element of word is punctuation
      print('\tJ', j)
      print('\t[WORD[J]]', word[j])
      # -------------------------------------------------------
      print('\tis Punctuation: ',word[j] in _remove)
      if word[j] in _remove:
        word = list(word)
        print('\t===> ',word, type(word))

        # [AND IF] if punctuation, word[j] is not between alphabets.
        if j == len(word)-1:
          print('\n\n************ last index of word  ***************')
          # [REMOVE]
          print('===============================')
          print(f'\tREMOVE {word[j]}')
          # word.remove(word[j])
          print(word[j])
          del word[j]
          print(word)
          # word -= str(word[j])
          print(f'\tAFTER REMOVE {word}')
          print('===============================')
          sentence[_index] = ''.join(word)
        elif 1 <= j <= len(word)-2:
          print('\n\n************  is between alphabets???  ***************')
          print('\n\t\INSIDE OF J range')
          print('\t\tWord[j-1]: ', word[j-2])
          print('\t\tWord[j+1]: ',word[j+1])
          if not word[j-1].isalpha() and word[j+1].isalpha():
            print('\t\tINDEX CHANGE success')
            # [REMOVE]
            print('===============================')
            print(f'\tREMOVE {word[j]}')
            print(word[j])
            del word[j]
            print(word)
            print(f'\tAFTER REMOVE {word}')
            print('===============================')
            sentence[_index] = ''.join(word)
      # [ELSE] if element of word is NOT punctuation ===> PASS

  return sentence

def main():
  print('The origin sentence was')
  sentence = ('Examples of contractions include: don’t, isn’t, and wouldn’t.').strip().split()
  print(onlyTheWords(sentence))
  print('-----------------------')
  print('Examples of contractions include: don’t, isn’t, and wouldn’t.')
  

if __name__ == '__main__':
  print(main())
  
'''