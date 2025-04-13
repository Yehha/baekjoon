import sys

T = int(sys.stdin.readline())

for i in range (T):

    str = sys.stdin.readline().strip()

    n = '0' if '0' in str else '1'

    splitStr = str.split(n)
    left = splitStr[0].count('!')
    right = splitStr[1].count('!')

    if right != 0:
        n = '1'

    if left % 2 == 1:
        if n == '0':
            n = '1'
        else:
            n = '0'
    
    print(n)
