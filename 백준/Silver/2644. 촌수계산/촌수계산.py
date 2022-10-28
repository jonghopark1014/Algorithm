import sys

def check(x, cnt):
    global ans_b, ans
    visited[x] = True
    if x == ans_b:
        ans = cnt
    for w in G[x]:
        if not visited[w]:
            cnt += 1
            check(w, cnt)
            cnt -= 1



N = int(sys.stdin.readline())
ans_a, ans_b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
G = [[] for _ in range(N+1)]
visited = [False] * (N+1)
ans = 0


for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    G[u].append(v)
    G[v].append(u)

check(ans_a, 0)

if ans == 0:
    print(-1)
else:
    print(ans)
