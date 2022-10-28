dp = [0] * 12

for tc in range(int(input())):
    N = int(input())
    for i in range(1, N + 1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 4
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[N])