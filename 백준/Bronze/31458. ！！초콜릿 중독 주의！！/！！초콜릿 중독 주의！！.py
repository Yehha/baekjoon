import sys

#1 수식 갯수 입력받기
N = int(sys.stdin.readline().strip()) 
    # int가 개행문자 무시 / but strip 습관들이기

for i in range (N):
    #2 데이터 입력받기
    data = sys.stdin.readline().strip()

    #3 정수 n 판별하기
    n = '0' if '0' in data else '1' # data에 0 있으면 n=0 else 1

    #4 문자열(n) 기준 분리해 갯수 세기
    split_data = data.split(n)
    left = split_data[0].count('!')
    right = split_data[1].count('!')

    #5 오른쪽 ! 으로 계산
    if right != 0:
        n = '1'

    #6 왼쪽 !으로 계산
    if left %2 == 1:
        n = '1' if n == '0' else '0'

    #7 결과 출력
    print(n)    
