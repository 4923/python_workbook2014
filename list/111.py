# Exercise 111: Only the Words

'''
Examples of contractions include: don’t, isn’t, and wouldn’t.
then your function should return the # list
["Examples", "of","contractions","include","don’t","isn’t","and","wouldn’t"].
'''

'''
0. 띄어쓰기 단위로 입력문장.split()
1. split()된 단어(type list)를 검사하여 특수문자 index 추출 할 것 (for문)
2. 특수문자 앞뒤.isalpha() == True 이면 지우지 말 것
3. 2가 아니면 지울 것
'''


def onlyTheWords(sentence):
  # [CHECK] spread elements assigned word in list named sentence
  for word in sentence:  # i is a string
    # [INDEX] index of word
    _index = sentence.index(word)
    for j in range(len(word)):
      # [IF] if element of word is punctuation
      if word[j] in _remove:
        word = list(word)
        # [IF IF] if punctuation assigned word[j] is NOT alphabets.
        if j == len(word)-1:
          # [REMOVE and refresh sentence]
          del word[j]
          sentence[_index] = ''.join(word)
        # [IF ELSE] if punctuation assigned word[j] is BETWEEN alphabets.
        elif 1 <= j <= len(word)-2:
          if not word[j-1].isalpha() and word[j+1].isalpha():
            # [REMOVE and refresh sentence]
            del word[j]
            sentence[_index] = ''.join(word)
      # [ELSE] if element of word is NOT punctuation ===> PASS
  return sentence # is a list

_remove = [',','.','?','-',"’",'"','!',';',':'] # define what is removable factor
def main():
  sentence = input("Input your sentence: ").strip().split() # assign user input as a list
  return onlyTheWords(sentence)
  

if __name__ == '__main__':
  print(main())