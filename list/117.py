# Exercise 117: Line of Best Fit

print('This is the program to calculate the line of best fit.')
status = True
xs, ys = [], []
while status:
  # 1. [INPUT] x와 y각각 받을 것.
  print('-------------------------------------------------------')
  print(f'This is your coordinate no.{len(xs)+1}')
  x = input('\tWhat is X value of coordinate?: ')
  y = input('\tWhat is Y value of coordinate?: ')
  print('Press enter to stop the program... ...')
  print('-------------------------------------------------------')

  # 2-1. 반복문 종료조건
  if x == '' or y == '':
    status = False
    #-----------------------------
    # 4. [OUTPUT] The line of best fit
    #-----------------------------
    best_line = f'y = {m:.2f} x + {b:.2f}'
    print(f'The FINAL line of best fit is {best_line}\n')
  # 2-2. 종료조건이 아닐 때 x는 xs에, y는 ys에 추가.
  else:
    xs.append(float(x))
    ys.append(float(y))
    # 이거 왜 추가한거지
    # xs = [float(x) for x in xs]
    # ys = [float(y) for y in ys]
  
    # 3. [Assign] calculate m, b
      #-----------------------------
      # 3-1 기초작업 [n, sigmaX, xPrime, sigmaX2, sigmaX_2]
      # ==> 하긴 했는데 결국 n과 평균값 (mean of X, Y) xPrime과 yPrime만 사용함
      #-----------------------------
    
    # n = x 또는 y들을 모은 list의 길이
    n = len(xs)

    # sigmaX: X들의 합
    sigmaX,sigmaY = sum(xs), sum(ys)

    # xPrime: x들의 평균
    xPrime, yPrime = sigmaX/n, sigmaY/n

    # sigmaXY= x*y들의 합
    # xyS = [(x*y) for x in xs for y in ys]
    xyS = [xs[i] * ys[i] for i in range(n)]
    sigmaXY = float(sum(xyS))

    # sigmaX2 = 시그마공식
    sigmaX2 =  (sigmaX * (sigmaX+1) * (2*sigmaX+1) )/6
    # sigmaX_2 = X들의 합을 제곱
    sigmaX_2 = (sigmaX) ** 2

      #-----------------------------
      # 3-2 [m] 계산
      #-----------------------------
    
    # 기울기 m의 분자 분모 각각 계산
    m1 = sum([(xs[i] - xPrime) * (ys[i] - yPrime) for i in range(n)])
    m2 = sum([(xs[i] - xPrime) ** 2 for i in range(n)])

    # 0으로 나눌 수 없으니 나누는 값이 0이면 m = 분자
    if m2 == 0:
      m = m1
    # 나누는값이 0이 아닐 때 m = m1 / m2
    else:
      m = m1/m2

      #-----------------------------
      # 3-3 [b] 계산
      #-----------------------------
    
    # b의 값 = y의 평균 - (m * x의 평균)
    b = yPrime - (m * xPrime )
    
    
    #-----------------------------
    # 4. [OUTPUT] The line of best fit
    #-----------------------------
    best_line = f'y = {m:.2f} x + {b:.2f}'
    print(f'==> The line of best fit is {best_line}\n')




