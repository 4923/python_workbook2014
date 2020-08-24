denomination = int(input("Input your denomination : ")) 
ind_of_banknote = {1:"George Washington",2:"Thomas Jefferson",5:"Abraham Lincoln",10:"Alexander Hamilton",20:"Andrew Jackson",50:"Ulysses S. Grant",100:"Benjamin Franklin"}
if denomination in ind_of_banknote:
  print(ind_of_banknote.get(denomination))
else:
  print("Wrong denomination of banknote. Try again")