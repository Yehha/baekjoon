import sys

#1 N줄 입력
while True :
    data = sys.stdin.readline().rstrip('\n')

    if not data:
        break

    #2 변수 생성
    small, capital, num, space = 0,0,0,0

    #3 문자열검사하기
    for char in data:
        if char.islower():
            small +=1
        elif char.isupper():
            capital +=1
        elif char.isdigit():
            num +=1
        else:
            space +=1

    print(small, capital, num, space)