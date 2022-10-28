import sys
from collections import deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def bfs(r, c, cnt, v):
    global ans
    Q = deque()
    Q.append([r, c, cnt, v])

    while Q:
        r, c, cnt, v = Q.popleft()
        for i in range(4):
            r2 = r + dr[i]
            c2 = c + dc[i]
            if 0 <= r2 < N and 0 <= c2 < N and not visited[r2][c2] and lst_N[r2][c2] == 0 and cnt < ans:
                visited[r2][c2] = True
                Q.append([r2, c2, cnt + 1, v])
            elif 0 <= r2 < N and 0 <= c2 < N and lst_N[r2][c2] != 0 and lst_N[r2][c2] != v:
                ans = min(ans, cnt)
                break


def changeMap(r, c):
    global chan_v
    Q2 = deque()
    Q2.append([r,c])
    lst_N[r][c] = chan_v

    while Q2:
        r, c = Q2.popleft()
        for i in range(4):
            r2 = r + dr[i]
            c2 = c + dc[i]
            if 0 <= r2 < N and 0 <= c2 < N and lst_N[r2][c2] == 1:
                lst_N[r2][c2] = chan_v
                Q2.append([r2, c2])


N = int(sys.stdin.readline())

lst_N = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 999999999

chan_v = 0

for r in range(N):
    for c in range(N):
        if lst_N[r][c] == 1:
            chan_v += 10
            changeMap(r, c)


for r in range(N):
    for c in range(N):
        if r - 1 >= 0 and lst_N[r][c] == 0 and lst_N[r - 1][c] != 0:
            visited = [[False] * N for _ in range(N)]
            bfs(r, c, 1, lst_N[r - 1][c])
        elif r + 1 < N and lst_N[r][c] == 0 and lst_N[r + 1][c] != 0:
            visited = [[False] * N for _ in range(N)]
            bfs(r, c, 1, lst_N[r + 1][c])
        elif c - 1 >= 0 and lst_N[r][c] == 0 and lst_N[r][c - 1] != 0:
            visited = [[False] * N for _ in range(N)]
            bfs(r, c, 1, lst_N[r][c - 1])
        elif c + 1 < N and lst_N[r][c] == 0 and lst_N[r][c + 1] != 0:
            visited = [[False] * N for _ in range(N)]
            bfs(r, c, 1, lst_N[r][c + 1])

print(ans)