import sys

def maxProfit(level, s):
    global ans
    if level + lst_N[level][0] -1 == N:
        ans = max(ans, s)
        return
    elif level + lst_N[level][0] -1 > N:
        s -= lst_N[level][1]
        ans = max(ans, s)
        return
    for idx in range(level + lst_N[level][0], N + 1):
        maxProfit(idx, s + lst_N[idx][1])


N = int(sys.stdin.readline())

lst_N = [[0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 0
for i in range(1, N + 1):
    if i + lst_N[i][0] - 1 <= N:
        maxProfit(i, lst_N[i][1])
print(ans)
