import sys

# N개 문자열(파일이름) 입력받기
N =  int(sys.stdin.readline()) # 입력받을 파일 갯수
data = [sys.stdin.readline().strip() for i in range(N)] # 파일 이름 리스트

result = [] #결과 문자열 저장할 리스트

# 첫 번째 문자열을 기준으로 동일한 위치의 문자를 비교
for i in range(len(data[0])):
    word = data[0][i] # 첫 번째 파일의 i번째 문자

    for j in range(1,len(data)): # 다른 파일들과 i번쨰 문자 비교
        if word != data[j][i]: # 하나라도 다르면 '?'로 변경
            word = '?'
            break
    result.append(word) # 결과 리스트에 추가


# 리스트를 문자열로 변환 후 출력
print(''.join(result))
