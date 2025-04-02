import sys

# 문자열 N줄 입력받아 리스트에 저장
N =  int(sys.stdin.readline()) # 입력받을 파일 이름 갯수
data = [sys.stdin.readline().strip() for i in range(N)] # 입력받은 파일 이름 리스트
result = [] #결과 값 담을 리스트

for i in range(len(data[0])):
    word = data[0][i] # 비교할 i번쨰 문자 
    for j in range(1,len(data)): # 다른 파일 이름들과 i번쨰 문자를 비교
        if word != data[j][i]:
            word = '?'
            break
    result.append(word)

print(''.join(result))