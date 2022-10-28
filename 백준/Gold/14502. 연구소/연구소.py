import sys
from collections import deque

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def safeZone(lst):
    global ans
    tmp_ans = 0
    for i in lst:
        tmp_ans += i.count(0)
    ans = max(tmp_ans, ans)

def installWall(idx, cnt):
    if cnt == 3:
        spreadVirus()
        safeZone(lst_N)
        Undo()
        return
    for i in range(idx, len(empty)):
        if not visited[i]:
            lst_N[empty[i][0]][empty[i][1]] = 1
            visited[i] = True
            installWall(i, cnt + 1)
            lst_N[empty[i][0]][empty[i][1]] = 0
            visited[i] = False


def spreadVirus():
    Q = deque()
    for i in virus:
        Q.append(i)

    while Q:
        r, c = Q.popleft()
        for i in range(4):
            r2 = r + dr[i]
            c2 = c + dc[i]
            if 0 <= r2 < R and 0 <= c2 < C and lst_N[r2][c2] == 0:
                lst_N[r2][c2] = 2
                Q.append([r2, c2])

def Undo():
    Q = deque()
    for i in virus:
        Q.append(i)

    while Q:
        r, c = Q.popleft()
        for i in range(4):
            r2 = r + dr[i]
            c2 = c + dc[i]
            if 0 <= r2 < R and 0 <= c2 < C and lst_N[r2][c2] == 2:
                lst_N[r2][c2] = 0
                Q.append([r2, c2])

    for i in virus:
        lst_N[i[0]][i[1]] = 2

R, C = map(int, sys.stdin.readline().split())

lst_N = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

ans = 0
virus = []
empty = []

for r in range(R):
    for c in range(C):
        if lst_N[r][c] == 0:
            empty.append([r, c])
        elif lst_N[r][c] == 2:
            virus.append([r, c])

visited = [False] * len(empty)

installWall(0, 0)

print(ans)