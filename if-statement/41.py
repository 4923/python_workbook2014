name_note = input("Input the name of note : ").upper()
note, octave = name_note[0], int(name_note[1]) # str type

# when 1 added to octave, frequency doubled
lst_note = ["C","D","E","F","G","A","B"]
lst_frequency = [261.63,293.66,329.63,349.23,392,440,493.88]

st_freq = lst_frequency[lst_note.index(note)] # standard freq
freq = st_freq / 2 ** (4 - octave)
print(f"The frequency of {name_note} is {freq:.2f}")
