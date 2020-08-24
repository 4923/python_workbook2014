# Exercise 118: Shuffling a Deck of Cards

# A is for 10
valsCard = ['2','3','4','5','6','7','8','9','T','J','Q','L','A']
shapesCard = ['s','h','d','c']

def createDeck():
  fullDecks = []
  for v in valsCard:
    for s in shapesCard:
      fullDecks.append(v+s)
  return fullDecks  # len(fullDecks): 52

import random

def shuffle():
  fullDecks = createDeck()
  for i in range(52):
    print('---------------------------------')
    print(f'Shuffle no.{i}')
    before = fullDecks[i]
    print(f'Before shuffle card: {before}')
    fullDecks[i] = fullDecks[random.randint(1,51)]
    after = fullDecks[i]
    print(f'After shuffle card: {after}')
    print('---------------------------------')
  return f'Shuffled deck: \n{fullDecks}'

def main():
  print(f'The origin deck: \n{createDeck()}')
  print(shuffle())

if __name__ == "__main__":
  main()