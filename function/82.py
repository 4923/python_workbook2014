# Exercise 82: Taxi Fare

def taxi_fare(travel_km):
  FARE_BARE = 4
  FARE_KM = 0.25
  total = FARE_BARE + FARE_KM * (travel_km - 0.14)
  return total

travel_km = float(input("How many kms did you traveled?: "))  # input
print(f"The total fare is {taxi_fare(travel_km)}") # output