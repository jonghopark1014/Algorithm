from collections import deque

def bfs(s, level):
    global ans
    Q = deque()
    Q.append([s, level])

    while Q:
        s, level = Q.popleft()
        if s > ans:
            continue
        if level == N:
           ans = s
        for i in range(N + 1):
            if G[level][i] != 0:
                Q.append([s + G[level][i], i])

for tc in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    G = [[0] * (N+1) for _ in range(N + 1)]
    ans = 99999
    for i in range(E):
        u, v, w = map(int, input().split())
        G[u][v] = w

    bfs(0, 0)
    print(f'#{tc}', ans)