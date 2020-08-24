# Exercise 84: Median of Three Values

a, b, c =  map(float, input("Input three numbers to find median val: ").split())  # input
def nums(a, b, c):
  sorted_nums = sorted([a, b, c])
  return sorted_nums[1]

print(f"The median val is {nums(a, b, c)}") # output