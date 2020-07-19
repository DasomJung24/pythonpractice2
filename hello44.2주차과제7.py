#7. Input 함수를 활용하여 아이디와 비밀번호가 일치하면 '로그인 성공' 틀리면 '로그인 실패' 문구가 나오는 코드를 작성하시오.



ID = 'ming'
PW = '0000'

while True :
    writeID = input('아이디를 입력하세요: ')
    writePW = input('비밀번호를 입력하세요: ')
    if writeID != ID or writePW != PW:
        print ('로그인 실패')
    if writeID == ID and writePW == PW:
        break
print ('로그인 성공')
