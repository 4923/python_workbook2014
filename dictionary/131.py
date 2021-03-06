# Exercise 131: Morse Code

'''
(* 15 줄 *)

모스 부호는 대시와 점을 사용하여 숫자와 문자를 나타내는 인코딩 체계입니다. 
이 연습에서는 문자와 숫자에서 모스 코드로의 매핑을 저장하기 위해 사전을 사용하는 프로그램을 작성합니다. 
마침표를 사용하여 점을 나타내고 하이픈을 사용하여 대시를 나타냅니다. 
문자와 숫자에서 대시와 점으로의 매핑은 표 [6.1] (https://link.springer.com/chapter/10.1007/978-3-319-14240-1_6#Tab1)에 나와 있습니다.

프로그램은 사용자로부터 메시지를 읽어야합니다. 
그런 다음 메시지의 각 문자와 숫자를 모스 부호로 변환하여 각 일련의 대시와 점 사이에 공백을 남겨 두어야합니다. 
프로그램은 문자 나 숫자가 아닌 문자를 무시해야합니다. Hello, World에 대한 모스 부호! 아래에 표시됩니다 :

......−...−..−−−.−−−−−.−..−..−..

모스 부호는 원래 전신 와이어를 사용하기 위해 19 세기에 개발되었습니다. 처음 만들어진 지 160 년이 지난 지금도 여전히 사용되고 있습니다.
'''

morse = { '.-'   : 'A',	'-...' : 'B',	'-.-.' : 'C',	'-..'  : 'D',	'.'    : 'E',	'..-.' : 'F',	'--.'  : 'G',	'....' : 'H',	'..'   : 'I',	'.---' : 'J', '-.-'  : 'K',	'.-..' : 'L',	'--'   : 'M',	'-.'   : 'N',	'---'  : 'O',	'.--.' : 'P',	'--.-' : 'Q',	'.-.'  : 'R',	'...'  : 'S',	'-'    : 'T',	'..-'  : 'U',	'...-' : 'V',	'.--'  : 'W',	'-..-' : 'X',	'-.--' : 'Y',	'--..' : 'Z' }
inv_morse = dict(map(reversed, morse.items()))

# [INPUT]
words = input('Write down a sentence you want to translate: ').upper()
translated = []
for i in range(len(words)):
  if words[i].isalpha():
    translated.append(inv_morse[words[i]])

# [OUTPUT]
result =''.join(translated)
print(result)