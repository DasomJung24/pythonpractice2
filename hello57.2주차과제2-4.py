'''
4. 1부터 100사이의 숫자를 하나 램덤하게 생성하고, 이를 맞추는 게임을 작성하세요.
  - 숫자 생성 후, 사용자가 숫자를 입력하면 둘을 비교하여 '높음','낮음','맞췄다'출력
  - 몇번의 guess 끝에 맞춘건지 시도한 횟수를 값을 출력
'''

import random

num = random.randint(1,100)
cycle = 1

while True:
    guess = int(input('숫자를 입력하세요: '))
    if num > guess :
        print('정답보다 낮음')
        cycle += 1
    elif num < guess :
        print('정답보다 높음')
        cycle += 1
    else :
        break
    
print('딩동댕')
print('guess횟수',cycle)
