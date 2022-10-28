from collections import deque

for tc in range(1, int(input()) + 1):
    N = int(input())
    lst_N = [list(input()) for _ in range(N)]
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    value = [[99999] * N for _ in range(N)]

    def bfs(r, c, cnt):
        Q = deque()
        Q.append([r, c, cnt])

        while Q:
            r, c, cnt = Q.popleft()
            if value[r][c] < cnt:
                continue
            for i in range(4):
                r2 = r + dr[i]
                c2 = c + dc[i]
                if 0 <= r2 < N and 0 <= c2 < N and cnt + int(lst_N[r2][c2]) < value[r2][c2]:
                    value[r2][c2] = cnt + int(lst_N[r2][c2])
                    Q.append([r2, c2, cnt + int(lst_N[r2][c2])])

    bfs(0, 0, 0)
    print(f'#{tc} {value[N-1][N-1]}')