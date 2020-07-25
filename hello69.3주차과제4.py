# 파일이름이 저장된 리스트에서 확장자가 .h 나 .c 인 파일을 화면에 출력하세요

list = ['intra.h', 'intra.c', 'define.h', 'run.py']

for i in list:
    if '.h' in i or '.c' in i:
        print(i)
    
