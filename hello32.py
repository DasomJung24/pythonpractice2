while True :
    print ('구구단을 출력합니다. 1에서 9까지의 숫자를 하나 입력하세요.')
    Dan = int(input())
    if ( Dan < 1 or Dan > 9 ) :
        print ('다시 입력해주세요.')
    if ( Dan > 0 and Dan <10 ) :
        break
count = 1
while True :
    print (Dan, '*', count, '=', Dan*count )
    count = count + 1
    if count == 10 :
        break
