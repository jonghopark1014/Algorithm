ans_lst = []

for tc in range(1, int(input()) + 1):
    day, month_0, month_3, year = map(int, input().split())
    lst_N = [0] + list(map(int, input().split()))
    dp = [0] * 13

    for i in range(1, 13):
        if i < 3:
            dp[i] = dp[i - 1] + min(lst_N[i] * day, month_0)
        else:
            dp[i] = min(dp[i-1] + min(lst_N[i] * day, month_0), dp[i-3] + month_3)

    if dp[12] < year:
        ans_lst.append(f'#{tc} {dp[12]}')
    else:
        ans_lst.append(f'#{tc} {year}')

print('\n'.join(ans_lst))

