import sys
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(r, c):
    Q = deque()
    Q.append([r, c])
    visited[r][c] = visited[r][c] + 1

    while Q:
        r, c = Q.popleft()
        for i in range(4):
            r2 = r + dr[i]
            c2 = c + dc[i]
            if 0 <= r2 < N and 0 <= c2 < M and maze_map[r2][c2] == '1' and visited[r2][c2] == 0:
                Q.append([r2, c2])
                visited[r2][c2] = visited[r][c] + 1

N, M = map(int, sys.stdin.readline().split())

maze_map = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

bfs(0, 0)

print(visited[N-1][M-1])