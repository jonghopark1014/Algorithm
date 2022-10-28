dp = [[] for _ in range(41)]

for tc in range(int(input())):
    N = int(input())
    for i in range(N + 1):
        if i == 0:
            dp[i] = (1, 0)
        elif i == 1:
            dp[i] = (0, 1)
        else:
            dp[i] = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])

    print(*dp[N])