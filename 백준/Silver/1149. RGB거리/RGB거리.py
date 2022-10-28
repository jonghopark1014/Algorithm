N = int(input())

lst_N = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0] = lst_N[0]

for r in range(1, N):
    for c in range(3):
        dp[r][c] = lst_N[r][c] + min(dp[r-1][(c+1) % 3], dp[r-1][(c+2) % 3])

print(min(dp[-1]))