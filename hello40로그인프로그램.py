#로그인프로그램/while문을이용해올바른암호를입력할때까지암호를입력받는프로그램작성.
#올바른암호를입력하면로그인성공을출력.

print ('암호를 입력하세요.')
secret = 'python'
answer = 0

while True :
    answer=input()
    if answer != secret:
        print('암호가 올바르지 않습니다.')
        print('암호를 입력하세요.')
    if answer == secret:
        break
print ('로그인 성공')
