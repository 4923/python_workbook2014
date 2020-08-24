# Exercise 86: The Twelve Days of Christmas

def ordinal_nums(num):  # exercise 85
  ordinal_nums = {1:'first', 2:'second', 3:'third', 4:'forth', 5:'fifth', 6:'sixth', 7:'seventh', 8:'eighth', 9:'ninth', 10:'tenth', 11:'eleventh', 12: 'twelfth'}
  return ordinal_nums[num]


gifts = ['partridge','turtle doves','French hens','calling birds','golden rings','geese a-laying','swans a-swimming','maids a-milking','ladies dancing','lords a-leaping','drummers drumming',
'pipers piping,']

def extra_lyrics(num):  # num == j in line 18
  return f"{ordinal_nums(num).title()} {gifts[num-1]}"

# output lyrics
def lyrics():
  # basic lyrics
  for i in range(1, 12):
    print(f"On the {ordinal_nums(i)} day of Christmas")
    print("my true love sent to me:")
    # changable lyrics
    for j in range(i):  
      if i == 1 and i-j == 1 : # last line (first day)
        print(f"A {gifts[0]} in a pear tree.")
      elif i-j == 1:  # last line (not first day)
        print(f"And a {gifts[0]} in a pear tree", end='')
        if i != 11:
          print('.')
        else:
          print("!")
      else: # iterate lyrics
        print(extra_lyrics(i-j))
    print("")

print(lyrics())