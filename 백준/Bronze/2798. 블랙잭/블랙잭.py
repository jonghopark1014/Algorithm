import sys

N, M = map(int, sys.stdin.readline().split())

lst_N = list(map(int, sys.stdin.readline().split()))

result = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sumV = lst_N[i] + lst_N[j] + lst_N[k]
            if sumV <= M:
                result += [sumV]
            sumV = 0

print(max(result))