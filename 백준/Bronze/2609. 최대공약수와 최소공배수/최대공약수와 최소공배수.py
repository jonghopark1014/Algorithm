import sys

N, M = map(int, sys.stdin.readline().split())

if N > M:
    N, M = M, N
a, b = N, M

while True:
    tempV = b % a
    if tempV == 0:
        break
    b = a
    a = tempV

GCD = a
LCM = int(N/a * M)
print(GCD)
print(LCM)
