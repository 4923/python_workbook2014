# remove the most extreme values
# Write a FUNCTION
# Function parameter: positive integer, n
# Function Performance: remove the largest n and the smallest n
# return value: the new copy of the list as the function's only result

# input: more than 4 values
# output: new list and origin list
# error message: if the input has less than 4 values

# input (convert input str to int) (make a list and sort)
experi_val = sorted(list(map(int, input("Input the values of science experiment: ").split())))

# function
def val_outliers(val, n):
  val = experi_val
  if len(val) < 4:
    return "Please input values more than 4"
  elif [a for a in val if a < 0] :
    return "Please input positive number"
  else:
    del val[:2], val[-2:]
    return f"The new list after removing outliers is {val}"

# output
print(val_outliers(experi_val,2))
print(f"The origin list of values is {experi_val}")