def dfs(r, c, value):
    global ans
    visited[c] = True
    if r == N - 1:
        if ans > value:
            ans = value
        return
    if ans < value:
        return
    for i in range(N):
        if not visited[i]:
            dfs(r+1, i, value + lst_N[r+1][i])
            visited[i] = False

ans_lst = []
for tc in range(1, int(input()) + 1):
    N = int(input())
    lst_N = [list(map(int, input().split())) for _ in range(N)]
    ans = 99 * 15
    for i in range(N):
        visited = [False] * N
        dfs(0, i, lst_N[0][i])
    ans_lst.append(f'#{tc} {ans}')

print('\n'.join(ans_lst))