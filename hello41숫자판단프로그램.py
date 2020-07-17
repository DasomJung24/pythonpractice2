#숫자판단프로그램/사용자로부터숫자를입력받아입력받은숫자보다작거나같은숫자중하나를무작위로선택해출력하는프로그램작성.
#입력받은숫자가1보다작으면'다시입력해주세요'라는메시지가출력되도록.

import random
print('숫자를 입력하세요.')
n = 0

while True :
    n = int(input())
    if n < 1:
        print('다시 입력해주세요.')
    if n >= 1:
        break
print('1부터 ' + str(n) + '까지에서 무작위로 선택된 값은 ' + str(random.randint(1,n)) + '입니다.')
