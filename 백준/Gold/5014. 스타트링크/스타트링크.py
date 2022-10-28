import sys
from collections import deque

def bfs(x, cnt):
    global U, D, ans
    Q = deque()
    Q.append([x, cnt])
    visited[x] = cnt

    while Q:
        x, cnt = Q.popleft()
        if x == G:
            ans = min(ans, cnt)
            break
        x2 = x + U
        x3 = x - D
        if 1 <= x2 < F + 1 and visited[x2] > cnt:
            Q.append([x2, cnt + 1])
            visited[x2] = cnt
        if 1 <= x3 < F + 1 and visited[x3] > cnt:
            Q.append([x3, cnt + 1])
            visited[x3] = 1

# 총 f층, 스타트링크 g 층, 강호 s층
F, S, G, U, D = map(int, sys.stdin.readline().split())
ans = 99999999
visited = [9999999] * (F + 2)

bfs(S, 0)

if ans == 99999999:
    print('use the stairs')
else:
    print(ans)