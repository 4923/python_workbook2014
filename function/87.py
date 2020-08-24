# Exercise 87: Center a String in the Terminal
# https://codechacha.com/ko/python-string-formatting/

def customed_form(_str,_width):  # str, int
  # result = print(f"{_str:*^WIDTH}") # error
  result = _str.center(_width)
  print(result, end='')
  print('end')

# input
_str = input("Input your string: ")
_width = int(input("Input the width: "))

# output
customed_form(_str,_width)