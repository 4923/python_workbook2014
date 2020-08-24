# Exercise 128: Reverse Lookup

def reverseLookup(_dict, _search):
  # https://hashcode.co.kr/questions/683/dict의-key-value를-뒤집는-방법
  inv_dict = {v:k for k, v in _dict.items()}
  # https://stackoverrun.com/ko/q/12961777
  # inv_dict = dict(map(reversed, _dict.items()))
  return inv_dict.get(_search)

def main():
  # key 하나에 여러개 val 넣으려면 [] 쓰면 된다는데 unhashable type error 생기고...
  # https://leti-lee.tistory.com/15
  # 이거 130에선 되는데 왜 여기선 안되는거
  dict_test = {'1':'one','2':['two', 'second'],'3':'three','4':'four'}

  # example 1: one key
  result_1 = reverseLookup(dict_test, 'one')

  # example 2: several keys
  result_2 = reverseLookup(dict_test, 'second')

  # example 3: no key
  result_3 = reverseLookup(dict_test, None)

  return result_1, result_2, result_3

if __name__ == "__main__":
  print(main())

