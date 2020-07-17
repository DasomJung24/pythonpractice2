#로또번호생성프로그램/while문을이용하여1-45사이의정수중6개를무작위로선택해출력.(중복가능)

import random

print ('로또번호 생성 프로그램')
print ('================')

count = 1
while count <= 6 :
    print (str(count) + '번째 번호는 ' + str(random.randint(1,45)) + '입니다.')
    count = count + 1
    
