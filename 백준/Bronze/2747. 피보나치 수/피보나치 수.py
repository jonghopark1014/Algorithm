dp = [0] * 46

value = int(input())
dp[1] = 1
dp[2] = 1
for i in range(3, value + 1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[value])