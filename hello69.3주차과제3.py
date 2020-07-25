# 임의의 체중과 신장을 입력한 후 비만도를 출력하는 함수를 작성하세요
# (BMI 공식활용 weight/height**2)

w = int(input('몸무게를입력하세요:'))
h = int(input('키를입력하세요:'))
bmi = w/((h*0.01)**2)

if bmi < 18.5 :
    print('마른체형입니다')
elif bmi >= 18.5 and bmi < 25.0 :
    print('표준입니다')
elif bmi >= 25.0 and bmi < 30.0 :
    print('비만입니다')
else :
    print('고도비만입니다')
