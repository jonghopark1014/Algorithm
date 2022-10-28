import sys
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def Cleaner(r, c ,dir):
    global ans
    Q = deque()
    Q.append([r, c, dir])

    while Q:
        r, c, dir = Q.popleft()
        for i in range(3, -1, -1):
            dir2 = (dir + i) % 4
            r2 = r + dr[dir2]
            c2 = c + dc[dir2]
            if 0 <= r2 < N and 0 <= c2 < M:
                if room[r2][c2] == 0 and not visited[r2][c2]:
                    visited[r2][c2] = True
                    room[r2][c2] = 99
                    ans += 1
                    Q.append([r2, c2, dir2])
                    break
        else:
            dir3 = (dir + 2) % 4
            r2 = r + dr[dir3]
            c2 = c + dc[dir3]
            if 0 <= r2 < N and 0 <= c2 < M and (room[r2][c2] == 1):
                break
            else:
                Q.append([r2, c2, dir])

N, M = map(int, sys.stdin.readline().split())

clean_r, clean_c, clean_dir = map(int, sys.stdin.readline().split())

room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
visited[clean_r][clean_c] = True
ans = 1

Cleaner(clean_r, clean_c, clean_dir)

print(ans)
