user_freq = float(input("Input the name of note : "))
 
lst_note = ["C","D","E","F","G","A","B"]
lst_frequency = [261.63,293.66,329.63,349.23,392,440,493.88]

for i, frequency in enumerate (lst_frequency):
  if frequency - 1  <= user_freq <= frequency + 1 :
    note = lst_note[i]
    print(f"The frequency {user_freq} is within {note+'4'}")
    break
  # to report error message only once
  elif i == (len(lst_frequency) -1):
    print(f"There is no frequency {user_freq} within the octave 4. Try again")
