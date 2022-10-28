def dfs(r, c, v):
    global ans
    if r == N-1:
        if v > ans:
            ans = v
        return
    if v <= ans:
        return
    if v == 0:
        return
    for i in range(N):
        if not visited[i] and lst_N[r+1][i] != 0:
            visited[i] = True
            dfs(r+1, i, v * (lst_N[r+1][i] / 100))
            visited[i] = False

for tc in range(1, int(input()) + 1):
    N = int(input())
    lst_N = []
    v_max = 0
    lst_N = [list(map(int, input().split())) for i in range(N)]
    ans = 0
    for i in range(N):
        if lst_N[i] != 0:
            visited = [False] * N
            visited[i] = True
            dfs(0, i, lst_N[0][i] / 100)
    ans *= 100
    print(f'#{tc} {ans:0.6f}')