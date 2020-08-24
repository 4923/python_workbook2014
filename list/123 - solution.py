# Exercise 123: Infix to Postfix

# infix = 일반적인 수식 표기법
# infix ex) (a+b) * c / d + e
# postfix = 연산자를 피연산자의 뒤에
# postfix ex)  a + b >> a b +
# *** 참고 (https://reakwon.tistory.com/62) ***

# infix = list(input('Input your mathmetical expression written in infix form: '))
infix = list('1 - 2 * 3 + (4 + 2) / 2') # input
infix = [e for e in infix if not e == ' '] # 불필요한 공백 제거
infix.append('0') # 마지막이 숫자일 수 밖에 없으니까 종료조건으로 문자열 0 추가
# [또는] infix = [e for e in input('Input your mathmetical expression written in infix form: ') if not e == ' '] # 한줄에 공백까지 제거

infix = [e for e in input('Input your mathmetical expression written in infix form: ') if not e == ' '] # 불필요한 공백 제거
infix.append('0') # 마지막이 숫자일 수 밖에 없으니까 종료조건으로 문자열 0 추가


# [조건] infix의 특정 부분이 + 또는 -기호일 때
def pm(infix, stack, post):
  print('**********************************************')
  print('\tthis is INFIX,', infix)
  stack.append(infix) # 1. + 또는 - 기호를 stack에 넣고
  print('\t',stack,'this is stack')
  if '(' in stack:  # ※ 괄호 읽는 중엔 (stack에 '('가 있을때) 안에 있는 연산자 처리 무시. 추가만하고 작업하지 않는다
    return stack, post
  for j in reversed(range(len(stack)-1)): # 2. stack을 자기자신을 제외하고 뒤에서부터 읽을 때
    print('\t\t현재 확인하고있는 stack[j]', stack[j])
    print('\t\t현재 확인하고있는 stack[j]의 인덱스 j ', j,'\n')
    if stack[j] == '+' or stack[j] == '-':  # 3. stack에 또다른 +나 -가 나오면
      print('\t\t[break condition] J is',j, 'stack[j] is', stack[j])
      print('\t\t 중단된 후의 값', ' '.join(post))
      break # 인덱스 읽는것 중단
    else: # 4. stack에 또다른 +가 나오지 않는다면
      print('\t\t----------------')
      print('\t\t [POP] stack 안의 기호 post에 이동 중')
      print('\t\t\t 추가하려는 인덱스 j는',j,'\t값 stack[j]는 ',stack[j])
      post.append(stack.pop(j)) # 4. stack 안의 기호를 post에 추가 할 것.
      # print('\t\t\t for에서 누락되었던 인덱스는',-1,' \t값 stack[-1]는 ',stack[-1])
      # post.append(stack.pop(-1))   # 역순이니까 -1 해야함
      print('\t\t 추가된 post 결과: ', post)
      print('\t\t----------------')
  print('**********************************************')
  return stack, post


# [조건] infix의 특정 부분이 * 또는 / 기호일 때
def md(infix, stack, post):
  stack.append(infix) # 1. * 또는 / 기호를 stack에 넣음 (빼는건 +나 -가 있을 때)
  print('\t\t [곱셈 나눗셈 그리고 (]',stack)
  return stack, post

# [조건] stack에 ( 를 넣은 후 ) 를 만났을 때
def bracket(infix, stack, post):
  for j in reversed(range(len(stack))):  # 3. 자기자신을 포함하여 stack를 뒤에서 읽다가
    print('\t\t [starting STACK]', stack)
    
    if stack[j] == '(':   # 4. ( 또는 ) 기호 만나면 중단하고, ( 또는 ) 기호를 삭제
      print(f'\t\t{stack[j]} will be deleted')
      del stack[j]
      print('\t\tdeleted stack is',stack)
      break
    else:   # 5. ( 만나기 전까지는 stack의 기호 post에 추가
      print('\t\t [STACK]', stack)
      print(f'\t\t{stack[j]} is where i am')
      post.append(stack.pop(j))
      print('\t\tNow post result is',post)
  return stack, post


## main
stack, post = [], []
for i in range(len(infix)):
  if i == len(infix)-1:
    print('--------------------------')
    print('         START FOR         ')
    print('\n')
    print('원래 값:',''.join(infix))
    print('검사 값:',infix[i])
    print('현재상황:',' '.join(post))
    print('목표 값:  1 2 3 * + 4 2 + 2 / -')
  if infix[i] == infix[-1]:   # 마지막 자리일 때
    print('FIXME-----------------')
    print('\tthis is i', i)
    print('\t총 길이',len(infix))
    # print(infix[12],infix[12],infix[-1],infix[i])
    print('\tThe last index')
    print('남은 stack',stack)  # 남은 stack 붓기 (있을때)
    print('남은 stack 길이',len(stack))
    if len(stack) >= 1:
      print('남은 stack 붓기 전 post',post)
      
      while True:
        if len(stack) == 0:
          break
        post.append(stack.pop())
      print('남은 stack 부은 후 post',post)
  
  elif infix[i].isdecimal() == True:
    print('\tthis is i', i)
    print('\t총 길이',len(infix))
    print(infix[12],infix[12],infix[-1],infix[i])
    post.append(infix[i])
    print(post)
  else:
    print(i,'th else statement')
    # stack.append(infix[i])
    # print('----------------')
    # print('\nthis is i', i)
    if infix[i] == '+' or infix[i] == '-':
      print('\t\tthis is +, -', i)
      pm(infix[i], stack, post)
    if infix[i] == '*' or infix[i] == '/' or infix[i] =='(':
      print('\t\tthis is x, /, (')
      md(infix[i], stack, post)
    if infix[i] == ')':
      print('\t\tthis is backet')
      bracket(infix[i], stack, post)
  if i == 10:
    print('\n')
    print('         END FOR         ')
    print('--------------------------')
    


    
  
print('\n===================================')
print(stack,'this is stack')
print(' '.join(infix),'this is infix')
print('\n[FINAL post]\t',' '.join(post))
print('[ANSWER infix]\t 1 2 3 * + 4 2 + 2 / -')