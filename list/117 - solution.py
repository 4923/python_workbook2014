# Exercise 117: Line of Best Fit
# 산점도와 추세선
# https://ko.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data/introduction-to-trend-lines/v/smoking-1945-extrapolation
# 선형 회귀?

'''
(* 41 라인 *)

가장 적합한 선은 n n의 모음에 가장 가까운 직선입니다.
데이터 점수. 이 연습에서는 컬렉션의 각 점에 x x가 있다고 가정합니다.
좌표와 y y
동등 어구. 기호 x¯ x¯
그리고 y¯ y¯
평균 x x를 나타내는 데 사용됩니다

컬렉션의 값과 평균 y y
컬렉션의 가치. 가장 적합한 선은 방정식 y = mx + b y = mx + b로 표현됩니다.

어디 m
그리고 b b
다음 공식을 사용하여 계산됩니다.

m = ∑xy− (∑x) (∑y) n∑x2− (∑x) 2n
m = ∑xy− (∑x) (∑y) n∑x2− (∑x) 2n
b = y¯−mx¯b = y¯−mx¯

사용자로부터 포인트 모음을 읽는 프로그램을 작성하십시오.
사용자는 첫 번째 좌표의 x 부분을 자체 행에 입력 한 다음 첫 번째 좌표의 y 부분을 자체 행에 입력합니다.
사용자가 x x를 사용하여 좌표를 계속 입력하도록 허용

그리고 y y
프로그램이 x x의 빈 줄을 읽을 때까지 각 줄에 입력 된 부분
동등 어구. 양식에 가장 적합한 선에 대한 공식을 표시하십시오.

y = mx + b
y = mx + b

m m을 교체함으로써
그리고 b b

위의 공식을 사용하여 계산 한 값으로 예를 들어, 사용자가 좌표를 입력하면

(1,1) (1,1), (2,2.1) (2,2.1) 과 (3,2.9) (3,2.9)
그러면 프로그램이 표시되어야합니다

y = 0.95x + 0.1
y = 0.95x + 0.1

'''

'''
필요한 값: x, y, x 평균, y 평균, 시그마x, 시그마y, 시그마xy(xy길이 합인가) / 시그마 x**2
1. [while] x와 y를 번갈아 받아서 list에 저장 (x 또는 y의 개수 알아야 함)
2. [break] if input == '': break
3. m과 b 계산하여 각각 할당
4. [return] 식 y = mx + b에 m과 b대입
'''

status = True
xs, ys = [], []
while status:
  # 1. [INPUT]
  x = input('What is X value of coordinate?: ')
  y = input('What is Y value of coordinate?: ')
  print(x)
  print(y)

  # 2. [BREAK condition], convert str to int
  if x == '' or y == '':
    status = False
  else:
    xs.append(float(x))
    print(xs)
    ys.append(float(y))
    print(ys)
    print('\n')

    xs = [float(x) for x in xs]
    ys = [float(y) for y in ys]
    print(xs, 'Is list of Xs')
    print(ys, 'Is list of Ys')
    print('\n')

  
  # 3. [Assign] calculate m, b
    #-----------------------------
    # 3-1 specific calculations
    #-----------------------------
  
  # n = x 또는 y들을 모은 list의 길이
  n = len(xs)
  print(n, 'is N: the number of data')
  print('\n')

  # sigmaX: X들의 합
  sigmaX,sigmaY = sum(xs), sum(ys)
  print(sigmaX, 'is Sigma X')
  print(sigmaY, 'is Sigma Y')
  print('\n')

  # xPrime: x들의 평균
  xPrime, yPrime = sigmaX/n, sigmaY/n
  print(xPrime, 'is average of Xs')
  print(yPrime, 'is average of Ys')
  print('\n')

  # sigmaXY= x*y들의 합
  # xyS = [(x*y) for x in xs for y in ys]
  xyS = [xs[i] * ys[i] for i in range(n)]
  sigmaXY = float(sum(xyS))
  print(sigmaXY, 'is sigma XY\n')

  # sigmaX2 = 시그마공식
  sigmaX2 =  (sigmaX * (sigmaX+1) * (2*sigmaX+1) )/6
  print(sigmaX2, 'is sigma (X**2)')
  # sigmaX_2 = X들의 합을 제곱
  sigmaX_2 = (sigmaX) ** 2
  print(sigmaX_2, 'is (sigmaX)**2')
  print('\n')
  print('--------------------------------')

    #-----------------------------
    # 3-2 calculate [m]
    #-----------------------------
  # 0으로 나눌 수 없으니 나누는 값이 0이면 m = 분자
  if (sigmaX2 - (sigmaX_2 / n)) == 0:
    m = sigmaXY - ( sigmaX * sigmaY / n)

  # 나누는값이 0이 아닐 때 m 계산
  else:
    m = (sigmaXY - ( sigmaX * sigmaY / n) ) / (sigmaX2 - (sigmaX_2 / n))
  print(m, 'is m')

  # NEW FROMULA
  print('#########################################################')
  m1 = sum([(xs[i] - xPrime) * (ys[i] - yPrime) for i in range(n)])
  print(m1, '========THIS IS M1============')
  m2 = sum([(xs[i] - xPrime) ** 2 for i in range(n)])
  print(m2, '========THIS IS M2============')
  if m2 == 0:
    m = m1
  else:
    m = m1/m2
  print(m2, '========THIS IS [    M     ]============')
  print('#########################################################')

    #-----------------------------
    # 3-3 calculate [b]
    #-----------------------------
  # b의 값 = y의 평균 - (m * x의 평균)
  b = yPrime - (m * xPrime )
  print(b, 'is b')
  print('\n')
  
  
  #-----------------------------
  # 4. [result] final formula is
  #-----------------------------
  best_line = f'y = {m:.2f} x + {b:.2f}'
  print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
  print(best_line)
  print('ANSWER== y = 0.95 x + 0.1')
  print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n')




