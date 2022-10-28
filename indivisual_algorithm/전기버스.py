def dfs(x):
    global cnt, ans
    if x >= N:
        if ans > cnt:
            ans = cnt
        return
    if cnt > ans:
        return
    for i in range(lst_N[x], 0, -1):
        cnt += 1
        dfs(x + i)
        cnt -= 1

ans_lst = []
for tc in range(1, int(input()) + 1):
    lst_N = list(map(int, input().split()))
    N = lst_N[0]
    ans = 9999
    cnt = 0
    for i in range(lst_N[1], 0, -1):
        dfs(1+i)
    ans_lst.append(f'#{tc} {ans}')
print('\n'.join(ans_lst))