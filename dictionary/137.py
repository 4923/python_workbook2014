# Exercise 137: Scrabble™ Score

'''
(* 해결됨 – 18 줄 *)
Scrabble ™ 게임에서 각 문자에는 관련 포인트가 있습니다. <<< 단어의 총점은 글자의 점수의 합입니다. >>>
더 일반적인 글자는 점수가 적지 만 덜 일반적인 글자는 점수가 높습니다. 
각 문자와 관련된 포인트는 다음과 같습니다.

단어에 대한 Scrabble ™ 점수를 계산하고 표시하는 프로그램을 작성하십시오. 
문자에서 포인트 값으로 매핑되는 사전을 만듭니다. 그런 다음 사전을 사용하여 점수를 계산하십시오.

Scrabble ™ 보드에는 글자 값 또는 전체 단어 값을 곱하는 사각형이 있습니다. 이 연습에서는이 사각형을 무시합니다.
'''

words = input('Input your word: ')
points = {'D':2, 'G':2, 'B':3, 'C':3, 'M':3, 'P':3, 'F':4, 'H':4, 'V':4, 'W':4, 'Y':4, 'K':5, 'J':8, 'X':8, 'Q':10, 'Z':10}
total = 0
for i in range(len(words)):
  if words[i].isalpha() == True and words[i].upper() in points:
    total += points[words[i].upper()]
print('The score is ', total)

