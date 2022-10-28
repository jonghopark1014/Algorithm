import sys

N = int(sys.stdin.readline())

maxV = 1

for i in range(1, N+1):  
    maxV *= i

print(maxV)