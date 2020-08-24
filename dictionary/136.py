# Exercise 136: Anagrams Again
anagram_1 = input('Input a message: ').upper().strip()
anagram_2 = input('Input another message: ').upper().strip()

def anagram_check(anagram):
  count, spell = 0, []
  while True:
    if anagram[count].isalpha() == True:
      spell.append(anagram[count])
    count += 1
    if count == len(anagram):
      return spell.sort()

def main():
  if anagram_check(anagram_1) == anagram_check(anagram_2):
    return 'Messages are anagram.'
  else:
    return 'Messages are NOT anagram.'

if __name__ == "__main__":
  print(main())

