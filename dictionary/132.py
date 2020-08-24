# Exercise 132: Postal Codes

def postal_check(provinces, postal_code):  # input str
  # 뒤집어서 사용해보고 싶은데 안뒤집어짐...
  # TypeError: unhashable type: 'list'
  # inv_provinces = dict(map(reversed, provnices.items()))
  # inv_provinces = {v:k for k, v in provinces.items()}

  # 우편번호 첫글자
  if postal_code[0] in provinces:
    city = provinces.get(postal_code[0])
  elif postal_code[0] in ['D', 'F', 'I', 'O', 'Q', 'U', 'W', 'Z']:
    print('Wrong Postal code. there is no valid beginning code.')

  # 우편번호 두번째 글자
  if postal_code[1] == 0:
    location = 'rural'
  else:
    location = 'urban'
  
  return f'{location} of {city}'
  
def main():
  # provinces = {'Newfoundland':	'A', 'Nova Scotia':'B', 'Prince Edward Island':'C', 'New Brunswick':'E', 'Quebec':	['G', 'H', 'J'], 'Ontario':['K', 'L', 'M', 'N', 'P'], 'Manitoba':'R', 'Saskatchewan':	'S', 'Alberta' :'T', 'British Columbia':	'V', 'Nunavut':'X', 'Northwest Territories':'X', 'Yukon':'Y'}
  provinces =  {'A': 'Newfoundland', 'B': 'Nova Scotia', 'C': 'Prince Edward Island', 'E': 'New Brunswick', 'G': 'Quebec', 'H': 'Quebec', 'J': 'Quebec', 'K': 'Ontario', 'L': 'Ontario', 'M': 'Ontario', 'N': 'Ontario', 'P': 'Ontario', 'R': 'Manitoba', 'S': 'Saskatchewan', 'T': 'Alberta', 'V': 'British Columbia', 'X': 'Nunavut or Northwest Territories', 'Y': 'Yukon'}

  # input str
  postal_code = input('What is your postal code?: ').upper()
  
  # output
  result = f'The postal code is for a {postal_check(provinces, postal_code)}'

  return result

if __name__ == "__main__":
  print(main())