# Exercise 114: Random Lottery Numbers

import random

# FUNCTION generate random/winning number 1~49
def generate_numbers():
  random_6, winning_6 = [], []
  while True:
    for _ in range(6):
      random_6.append(random.randint(1,49))
      winning_6.append(random.randint(1,49))
    # 중복 방지 set
    if len(set(random_6)) and len(set(winning_6)) == 6:
      return [random_6, winning_6]
    # 중복이 있을 경우 list 초기화
    else:
      random_6, winning_6 = [], []

# check winning condition
def ifWin(random_6, winning_6):
  if random_6 == winning_6:
    return True # 6자리 모두 같을 때, 당첨
  else:
    return False  # 당첨되지 않음.
  
def main():
  random_6, winning_6 = generate_numbers()
  if ifWin(random_6, winning_6) == True:
    result = f'''Congratulations! You are on the top prize in the lottery.
    The winning number was {sorted(winning_6)}"'''
  else:
    result = f'''Try next time!
    The winning number was {sorted(winning_6)}'''
  return result

if __name__ == "__main__":
  print(main())