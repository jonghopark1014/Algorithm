import sys

def knapsack(idx):
    if idx == N + 1:
        return
    for i in range(K + 1):
        if lst_thing[idx][0] > i:
            dp[idx][i] = dp[idx - 1][i]
        else:
            dp[idx][i] = max(dp[idx - 1][i], lst_thing[idx][1] + dp[idx-1][i-lst_thing[idx][0]])

    knapsack(idx + 1)

N, K = map(int, sys.stdin.readline().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]

lst_thing = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

knapsack(0)

print(dp[N][K])