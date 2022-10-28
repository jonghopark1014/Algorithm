import sys

N, K = map(int, sys.stdin.readline().split())
lst_n = [0] +list(map(int, sys.stdin.readline().split()))

for i in range(1, len(lst_n)):
    lst_n[i] = lst_n[i] + lst_n[i-1]

sumV = 0
maxV = -0xffffffff
for j in range(K, len(lst_n)):
    sumV = lst_n[j] - lst_n[j-K]
    if maxV < sumV:
        maxV = sumV
    sumV = 0

print(maxV)