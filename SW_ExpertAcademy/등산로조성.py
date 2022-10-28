dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]

def dfs(r, c, k, cnt, prev, order):
    global ans
    if ans < cnt:
        ans = cnt
    for i in range(4):
        r2 = r + dr[i]
        c2 = c + dc[i]
        if 0 <= r2 < N and 0 <= c2 < N:
            if lst_N[r2][c2] < prev and not visited[r2][c2]:
                visited[r2][c2] = True
                dfs(r2, c2, k, cnt + 1, lst_N[r2][c2], order)
                visited[r2][c2] = False
            elif k and lst_N[r2][c2] - prev < k and not visited[r2][c2] and lst_N[r2][c2] - 1 >= 0 and order:
                visited[r2][c2] = True
                dfs(r2, c2, k - 1 - lst_N[r2][c2] + prev, cnt + 1, prev - 1, order - 1)
                visited[r2][c2] = False
    return

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    lst_N = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    max_lst = []
    max_v = 0
    for r in lst_N:
        value = max(r)
        if value > max_v:
            max_v = value

    for r in range(N):
        for c in range(N):
            if lst_N[r][c] == max_v:
                max_lst.append([r, c])

    for r, c in max_lst:
        visited = [[False] * N for _ in range(N)]
        visited[r][c] = True
        dfs(r, c, K, 1, lst_N[r][c], 1)

    print(f'#{tc}', ans)
