from collections import deque

T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def Move(r, c, value):
    ans = 1
    Q = deque()
    Q.append([r, c, value])

    while Q:
        r, c, value = Q.popleft()
        for i in range(4):
            r2 = r + dr[i]
            c2 = c + dc[i]
            if 0 <= r2 < N and 0 <= c2 < N and room[r2][c2] == room[r][c] + 1:
                ans += 1
                Q.append([r2, c2, room[r2][c2]])

    return ans

for tc in range(1, T+1):
    tmp_lst = []
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    max_room = 0
    max_len = 0
    for r in range(N):
        for c in range(N):
            ans = Move(r, c, room[r][c])
            if max_len < ans:
                max_room = room[r][c]
                max_len = ans
            elif max_len == ans:
                if max_room > room[r][c]:
                    max_room = room[r][c]

    print(f'#{tc}', max_room, max_len)