#6.로또번호 6개를 무작위로 생성하세요(1~45)(중복x)


import random

lotto = random.sample(range(1,46), 6)
print(lotto)
