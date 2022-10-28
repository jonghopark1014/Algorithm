import sys

N = int(sys.stdin.readline())


for i in range(N):
    temp = sum(map(int, str(i)))
    result = i + temp
    if result == N:
        print(i)
        break
else:
    print(0)