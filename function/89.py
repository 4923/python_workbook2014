# Exercise 89: Capitalize It
# example) what time do i have to be there? what's the address?

def _Capitzlize_it(message):
  new_message = message # copy
  new_message[0] = message[0].upper() #Capitalize first letter

  for index in range(len(message)-2):
    # Capitzlize 'i'
    if message[index] == 'i' and message[index-1] == ' ':
      new_message[index] = message[index].upper()
    # Capitalize first alpha
    if (message[index] == '.' or '!' or'?') and (message[index+2] == ' ') :
      new_message[index+2] = message[index+2].upper()
  return "".join(new_message)

# message = list(input("Typing... ")) # input
message = list('what time do i have to be there? whats the address?')
print(_Capitzlize_it(message))  # output