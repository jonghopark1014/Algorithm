from collections import deque

T = int(input())

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    global house, ans
    Q = deque()
    Q.append([r, c])
    visited[r][c] = 1
    tmp_v = 1

    while Q:
        r, c = Q.popleft()
        if tmp_v != visited[r][c]:
            tmp_p = (M * house) - ((visited[r][c] ** 2) + ((visited[r][c]-1)**2))
            if tmp_p >= 0 and ans < house:
                ans = house
            tmp_v += 1

        for i in range(4):
            r2 = r + dr[i]
            c2 = c + dc[i]
            if 0 <= r2 < N and 0 <= c2 < N and not visited[r2][c2]:
                visited[r2][c2] = visited[r][c] + 1
                if not mapping[r2][c2]:
                    Q.append([r2, c2])
                else:
                    Q.append([r2, c2])
                    house += 1


for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 1은 집
    mapping = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for r in range(N):
        for c in range(N):
            visited = [[0] * N for _ in range(N)]
            house = 0
            if mapping[r][c] == 1:
                house += 1
            bfs(r, c)
    if ans == 0:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', ans)
