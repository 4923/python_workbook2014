# Exercise 83: Shipping Calculator

num_items = int(input("How many items did you buy?: ")) # input

def shipping_charge(num_items):
  BASE = 10.95  # unit $
  EXTRA = 2.95  # unit $
  shipping_charge = BASE + EXTRA * (num_items - 1)
  return shipping_charge

print(f"Your shipping charge is ${shipping_charge(num_items):.2f}") # output
