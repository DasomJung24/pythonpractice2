# 중첩반복문을 사용하여 신문을 배달하는 프로그램을 작성하세요. 단 미납금이 있는 호수에는 배달x

apt = [[101,102,103,104],[201,202,203,204],[301,302,303,304],[401,402,403,404]]
unpaid = [101,202,302,403]

for a in apt :
    for b in a :
        if b in unpaid :
            print(b,': 미납')
        else :
            print(b,': 배달')
