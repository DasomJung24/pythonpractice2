# 자연수 n을 입력하고, 자연수 n의 약수들의 총 합을 구하시오

n = int(input('쟈연수를입력하세요:'))
a = 1
sum = 0

while n >= a :
    if n % a == 0 :
        sum += a
    a = a + 1

print(sum)
