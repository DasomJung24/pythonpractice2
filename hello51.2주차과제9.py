#두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오

A = int(input('정수A를 입력하세요: '))
B = int(input('정수B를 입력하세요: '))

if A > B :
    print(A,'>',B)
elif A < B :
    print(A,'<',B)
else :
    print(A,'=',B)
