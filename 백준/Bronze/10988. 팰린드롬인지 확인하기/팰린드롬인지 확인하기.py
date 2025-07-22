import sys 
data = sys.stdin.readline().strip()

print(1 if data == data[::-1] else 0)