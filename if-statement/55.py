# Exercise 55: Frequency to Name

'''
Write a program that reads
the frequency of the radiation from the user
and displays the appropriate name.
'''

freq = int(input("Input the frequency range(Hz): "))

if freq < 3*10**9:
  name_freq = 'Radio waves'
elif 3*10**9 < freq < 3*10**12:
  name_freq = 'Microwaves'
elif 3*10**12 < freq < 4.3*10**14:
  name_freq = 'Microwaves'
elif 4.3*10**14 < freq < 7.5*10**14:
  name_freq = 'Microwaves'
elif 7.5*10**14 < freq < 3*10**17:
  name_freq = 'Microwaves'
elif 3*10**17 < freq < 3*10**19:
  name_freq = 'Microwaves'
elif 3*10**19 < freq :
  name_freq = 'Microwaves'