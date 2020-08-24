# Exercise 65: Compute the Perimeter of a Polygon

x1 = input("Enter the x part of the coordinate: ")
y1 = input("Enter the y part of the coordinate: ")
origin_x, origin_y = x1, y1
perimeter = 0
while True:
  x2 = input("Enter the x part of the coordinate: (blank to quit): ")
  if x2 == "":
    perimeter += ((float(origin_x)-float(x1))**2 + (float(origin_y)-float(y1))**2 ) ** 0.5
    print(f"The perimeter of that polygon is {perimeter}")
    break
  else:
    y2 = input("Enter the y part of the coordinate: ")
    # 왜 ** 1/2 값이 이상하게 나오는지 모르겠네
    perimeter += ((float(x2)-float(x1))**2 + (float(y2)-float(y1))**2 ) ** 0.5
    x1, y1 = x2, y2


  