side1, side2, side3 = map(int,input('Input 3 lengths of side : ').split())
if side1 == side2 == side3:
  print("the triangle is equilateral")
elif side1 == side2 or side1 == side3 or side2 == side3:
  print("the triangle is isosceles")
else:
  print("the triangle is scalene")

# map = map(변환함수, 순회 가능한 데이터)
# 입력을 list로 받기
# 1. str로 저장 : input().split() 
# 2. int로 저장 : list(map(int,input().split()))
# lst_sides = list(map(int,input().split()))