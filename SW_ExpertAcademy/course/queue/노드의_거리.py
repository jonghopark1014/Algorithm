T = int(input())

def BFS(s):
    global G
    visited = [0] * (V+1)
    Q = [s]
    visited[s] = 1
    while Q:
        v = Q.pop(0)
        for w in G[v]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[v] + 1
    if visited[Y] -1 == -1:
        print(0)
    else:
        print(visited[Y]-1)

for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    S, Y = map(int, input().split())
    print(f'#{tc}', end = ' ')
    BFS(S)