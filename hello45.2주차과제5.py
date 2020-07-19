#5. 1~30 사이의 수에서 홀수만 더한 값, 짝수만 더한 값 구하시오(while 문 활용)

x = 1
sum_even = 0
sum_odd = 0

while x < 31:
    if x % 2 == 0 :
      sum_even = sum_even + x
    else :
      sum_odd = sum_odd + x
    x = x + 1
      
print('짝수만 더한 값은',sum_even,'입니다.')
print('홀수만 더한 값은',sum_odd,'입니다.')
