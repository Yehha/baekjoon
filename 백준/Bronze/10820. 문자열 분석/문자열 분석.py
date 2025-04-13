import sys

#1 N줄 입력
while True :
    data = sys.stdin.readline().rstrip('\n')

    if not data:
        break

    #2 변수 생성
    small, capital, num, space = 0,0,0,0

    #3 문자열 검사
    for char in data:
        if char.islower():    #소문자
            small +=1
        elif char.isupper():  #대문자
            capital +=1
        elif char.isdigit():  #숫자
            num +=1
        else:                 #공백
            space +=1

    #4 결과 출력
    print(small, capital, num, space)
