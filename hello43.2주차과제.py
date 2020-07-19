#1. 숫자 입력하면 구구단을 실행하는 코드를 작성하시오.

print ('숫자를 입력하세요.')
Dan = 0
num = 1

Dan = int(input())
while num <= 9 :        
    print (Dan, '*', num, '=', Dan*num)
    num = num + 1
