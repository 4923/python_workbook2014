

def hex2int(num): # str, upper
  if num.isdigit() == True and 1 <= int(num) <= 9:
    num_in_hex = int(num)
  elif num.isalpha() == True:
    _hex = {'A': 10,'B':11,'C':12,'D':13,'E':14,'F':15}
    alp_in_hex = _hex[num]
  else:
    print("Invalid input. Try again")
  return num_in_hex + alp_in_hex

def int2hex(num): # int
  if num.isalpha() == True:
    num = int(num)
    _16s = num / 16
    if _16s ** 1/2: # 쓰다 말았음
      return