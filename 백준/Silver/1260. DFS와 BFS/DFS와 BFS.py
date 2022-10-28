import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

G = [[] for _ in range(N+1)]
visited_dfs = [0] * (N+1)
visited_bfs = [0] * (N+1)

for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    G[u].append(v)
    G[v].append(u)

for i in range(len(G)):
    G[i].sort()

def dfs(v):
    visited_dfs[v] = 1
    print(v, end = ' ')
    for w in G[v]:
        if not visited_dfs[w]:
            dfs(w)

def bfs(v):
    Q = deque()
    Q.append(v)
    visited_bfs[v] = 1

    while Q:
        v2 = Q.popleft()
        print(v2, end=' ')
        for w in G[v2]:
            if visited_bfs[w] == 0:
                Q.append(w)
                visited_bfs[w] = 1
dfs(V)
print()
bfs(V)