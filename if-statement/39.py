var = input("Input decibel or noise that you want to know : ")

if type(var) == "<class 'int'>":
  print("this is int type")

jackhammer = 106 < var <= 130
gas_lawnmower = 70 < var <= 106
alarm_clock = 40 < var <= 70
Quiet_room = var == 40
noises = [jackhammer,gas_lawnmower,alarm_clock,Quiet_room]

if var < 40:
  print("The decibel level is quieter than quiet room")
elif var > 130:
  print("The decibel level is louder than jackhammer")


  # ??? 입력이 숫자일때랑 문자일때 둘 다 활용해야하는데 구분을 어떻게 하지?

