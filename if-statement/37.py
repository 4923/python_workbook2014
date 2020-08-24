sides = int(input("How many sides does the shape have? (3 to 10) : "))
shapes = {3:"triangle",4:"quadrilateral",5:"pentagon",6:"hexagon",7:"heptagon",8:"octagon",9:"nonagon",10:"decagon"}
if sides < 3 or sides > 10:
  print("Wrong number. Please input the number between 3 to 10")
else:
  print(f"The name of shape is {shapes[sides]}")