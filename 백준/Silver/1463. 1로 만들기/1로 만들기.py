N = int(input())

dp = [0] * (10**6 + 1)

dp[2] = 1
dp[3] = 1

for i in range(4, N + 1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i // 2] + 1
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i // 3] + 1

print(dp[N])