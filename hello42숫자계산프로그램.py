#숫자계산프로그램/while문을이용해숫자를입력받다가'입력 끝'을입력하면지금까지입력받은숫자들의합,평균,최대값,최소값을출력하는프로그램작성.

print('숫자를 입력하세요.')
n = 0
sum = 0
end = '입력 끝'

while True :
    n = input()
    if n == end :
        print ('입력받은 숫자들의 합은 ' + str(sum(int(n))))
    
