# Exercise 123: Infix to Postfix

# infix = 일반적인 수식 표기법
# infix ex) (a+b) * c / d + e
# postfix = 연산자를 피연산자의 뒤에
# postfix ex)  a + b >> a b +
# *** 참고 (https://reakwon.tistory.com/62) ***

infix = [e for e in input('Input your mathmetical expression written in infix form: ') if not e == ' '] # 불필요한 공백 제거
infix.append('0') # 마지막이 숫자일 수 밖에 없으니까 종료조건으로 문자열 0 추가
print(infix)


# 함수조건
# [조건] infix의 특정 부분이 + 또는 -기호일 때
def pm(infix, stack, post):
  stack.append(infix) # 1. + 또는 - 기호를 stack에 넣고
  if '(' in stack:  # ※ 괄호 읽는 중엔 (stack에 '('가 있을때) 안에 있는 연산자 처리 무시. 추가만하고 작업하지 않는다
    return stack, post
  for j in reversed(range(len(stack)-1)): # 2. stack을 자기자신을 제외하고 뒤에서부터 읽을 때
    if stack[j] == '+' or stack[j] == '-':  # 3. stack에 또다른 +나 -가 나오면
      break # 인덱스 읽는것 중단
    else: # 4. stack에 또다른 +가 나오지 않는다면
      post.append(stack.pop(j)) # 4. stack 안의 기호를 post에 추가 할 것.
      # post.append(stack.pop(-1))   # 역순이니까 -1 해야함
  return stack, post


# [조건] infix의 특정 부분이 * 또는 / 기호일 때
def md(infix, stack, post):
  stack.append(infix) # 1. * 또는 / 기호를 stack에 넣음 (빼는건 +나 -가 있을 때)
  return stack, post

# [조건] stack에 ( 를 넣은 후 ) 를 만났을 때
def bracket(infix, stack, post):
  for j in reversed(range(len(stack))):  # 3. 자기자신을 포함하여 stack를 뒤에서 읽다가
    if stack[j] == '(':   # 4. ( 또는 ) 기호 만나면 중단하고, ( 또는 ) 기호를 삭제
      del stack[j]
      break
    else:   # 5. ( 만나기 전까지는 stack의 기호 post에 추가
      post.append(stack.pop(j))
  return stack, post


## main
def main():
  print('main')
  stack, post = [], []
  for i in range(len(infix)):
    print(i)
    print()
    print(' '.join(infix), 'is origin infix')
    print(' '.join(post), 'is post')
    print(stack, 'is stack')
    if infix[i] == '0':
      break

    if infix[i] == infix[-1]:   # 마지막 자리일 때
      while True:
        if len(stack) != 0:   # stack이 있다면
          post.append(stack.pop())  # [POP] 남은 stack 붓고
    
    if infix[i].isdecimal() == True:
      post.append(infix[i])

    else:
      if infix[i] == '+' or infix[i] == '-':
        pm(infix[i], stack, post)
      if infix[i] == '*' or infix[i] == '/' or infix[i] =='(':
        md(infix[i], stack, post)
      if infix[i] == ')':
        bracket(infix[i], stack, post)
      
  return print(' '.join(post))

if __name__ == '__main__':
  main()