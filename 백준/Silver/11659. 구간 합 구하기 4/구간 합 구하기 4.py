import sys

N, M = map(int,sys.stdin.readline().split())

lst_N = list(map(int, sys.stdin.readline().split()))
lst_M = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

sumV = 0
for i in range(len(lst_N)):
    sumV += lst_N[i]
    lst_N[i] = sumV
lst_N.insert(0, 0)

for j in lst_M:
    print(lst_N[j[1]] - lst_N[j[0]-1])