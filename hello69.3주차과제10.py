# 자판기 알고리즘을 짜시오
# 자판기 내의 음식이나 음료의 종류는 2가지 이상(한번에 같은음료 선택가능)
# 잔돈계산하는 알고리즘도함께.(최대 3가지만 선택)

VendingM = {'jelly':200,'candy':100,'gum':500,'coke':700,'sprite':800}

cash = int(input('금액을투입하세요:'))
n = 1


while n <= 3 :
    a = VendingM[input('선택하세요:')]
    cash = cash - a
    if  cash >= 100 or cash > a:
        print(a,'결제,','잔돈',cash)
        n = n + 1
    elif cash == 0 :
        print('잔돈',0)
        break
    elif cash < a:
        print('돈이부족합니다','잔돈',cash+a)
        break
