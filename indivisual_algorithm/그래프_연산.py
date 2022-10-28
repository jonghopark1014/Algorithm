from collections import deque

cal = [1, -1, '*', -10]

def bfs(value, cnt):
    Q = deque()
    Q.append([value, cnt])

    while Q:
        v, cnt = Q.popleft()
        if v == M:
            break
        for i in range(4):
            if i == 2:
                v2 = v * 2
            else:
                v2 = v + cal[i]
            if 0 <= v2 < 1000001 and not visited[v2]:
                visited[v2] = True
                Q.append([v2, cnt + 1])

    return cnt

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    visited = [False] * 1000001
    print(f'#{tc}', bfs(N, 0))

