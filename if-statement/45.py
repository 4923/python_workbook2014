position = input("Input the position : ")
row, col = position[0], position[1]
# 보드가 더 커졌을 경우 ex) row가 h 이상일 경우엔 검사할 수 없음.
# 따라서 보드에 규칙을 찾아서 검사해야함.
row = ["a","b","c","d","e","f","g","h"].index(row) + 1

board_lst =[ [x+1 for x in range(8)] for x in range(8)  ]

for i in range(8):  # type(i) = letter, row index
  for j in range(8):  # type(j) = number, col index
    if (i+1) % 2 != 0:  # row a, c, e, g
      if (j+1) % 2 != 0:  # col 1, 3, 5, 7
        color = "black"
        break
      else: # col 2, 4, 6, 8
        color = "white"
        break
      break

    else: # row b, d, f, h
      if (j+1) % 2 != 0:  # col 1, 3, 5, 7
        color = "white"
        break
      else: # col 2, 4, 6, 8
        color = "black"
        break
      break

print(f"color of {position} is {color}")  