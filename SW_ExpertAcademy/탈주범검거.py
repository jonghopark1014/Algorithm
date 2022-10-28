from collections import deque

T = int(input())

#  하 상 우 좌
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

dic_pipe = {
    'down' : [1, 2, 4, 7],
    'up' : [1, 2, 5, 6],
    'left' : [1, 3, 4, 5],
    'right' : [1, 3, 6, 7]
}


def Escape(r, c):
    Q = deque()
    Q.append([r, c])
    cnt = 0

    while Q:
        r, c = Q.popleft()
        if underground[r][c] == 1:
            # 하
            r2 = r + dr[0]
            c2 = c + dc[0]
            if 0 <= r2 < N and 0 <= c2 < M and not visited[r2][c2] and underground[r2][c2] in dic_pipe['down']:
                Q.append([r2, c2])
                visited[r2][c2] = visited[r][c] + 1
            # 상
            r2 = r + dr[1]
            c2 = c + dc[1]
            if 0 <= r2 < N and 0 <= c2 < M and not visited[r2][c2] and underground[r2][c2] in dic_pipe['up']:
                Q.append([r2, c2])
                visited[r2][c2] = visited[r][c] + 1
            # 우
            r2 = r + dr[2]
            c2 = c + dc[2]
            if 0 <= r2 < N and 0 <= c2 < M and not visited[r2][c2] and underground[r2][c2] in dic_pipe['right']:
                Q.append([r2, c2])
                visited[r2][c2] = visited[r][c] + 1
            # 좌
            r2 = r + dr[3]
            c2 = c + dc[3]
            if 0 <= r2 < N and 0 <= c2 < M and not visited[r2][c2] and underground[r2][c2] in dic_pipe['left']:
                Q.append([r2, c2])
                visited[r2][c2] = visited[r][c] + 1
        elif underground[r][c] == 2:
            # 하
            r2 = r + dr[0]
            c2 = c + dc[0]
            if 0 <= r2 < N and 0 <= c2 < M and not visited[r2][c2] and underground[r2][c2] in dic_pipe['down']:
                Q.append([r2, c2])
                visited[r2][c2] = visited[r][c] + 1
            # 상
            r2 = r + dr[1]
            c2 = c + dc[1]
            if 0 <= r2 < N and 0 <= c2 < M and not visited[r2][c2] and underground[r2][c2] in dic_pipe['up']:
                Q.append([r2, c2])
                visited[r2][c2] = visited[r][c] + 1
        elif underground[r][c] == 3:
            # 좌
            r2 = r + dr[3]
            c2 = c + dc[3]
            if 0 <= r2 < N and 0 <= c2 < M and not visited[r2][c2] and underground[r2][c2] in dic_pipe['left']:
                Q.append([r2, c2])
                visited[r2][c2] = visited[r][c] + 1
            # 우
            r2 = r + dr[2]
            c2 = c + dc[2]
            if 0 <= r2 < N and 0 <= c2 < M and not visited[r2][c2] and underground[r2][c2] in dic_pipe['right']:
                Q.append([r2, c2])
                visited[r2][c2] = visited[r][c] + 1
        elif underground[r][c] == 4:
            # 상
            r2 = r + dr[1]
            c2 = c + dc[1]
            if 0 <= r2 < N and 0 <= c2 < M and not visited[r2][c2] and underground[r2][c2] in dic_pipe['up']:
                Q.append([r2, c2])
                visited[r2][c2] = visited[r][c] + 1
            # 우
            r2 = r + dr[2]
            c2 = c + dc[2]
            if 0 <= r2 < N and 0 <= c2 < M and not visited[r2][c2] and underground[r2][c2] in dic_pipe['right']:
                Q.append([r2, c2])
                visited[r2][c2] = visited[r][c] + 1
        elif underground[r][c] == 5:
            # 하
            r2 = r + dr[0]
            c2 = c + dc[0]
            if 0 <= r2 < N and 0 <= c2 < M and not visited[r2][c2] and underground[r2][c2] in dic_pipe['down']:
                Q.append([r2, c2])
                visited[r2][c2] = visited[r][c] + 1
            # 우
            r2 = r + dr[2]
            c2 = c + dc[2]
            if 0 <= r2 < N and 0 <= c2 < M and not visited[r2][c2] and underground[r2][c2] in dic_pipe['right']:
                Q.append([r2, c2])
                visited[r2][c2] = visited[r][c] + 1
        elif underground[r][c] == 6:
            # 하
            r2 = r + dr[0]
            c2 = c + dc[0]
            if 0 <= r2 < N and 0 <= c2 < M and not visited[r2][c2] and underground[r2][c2] in dic_pipe['down']:
                Q.append([r2, c2])
                visited[r2][c2] = visited[r][c] + 1
            # 좌
            r2 = r + dr[3]
            c2 = c + dc[3]
            if 0 <= r2 < N and 0 <= c2 < M and not visited[r2][c2] and underground[r2][c2] in dic_pipe['left']:
                Q.append([r2, c2])
                visited[r2][c2] = visited[r][c] + 1
        elif underground[r][c] == 7:
            # 상
            r2 = r + dr[1]
            c2 = c + dc[1]
            if 0 <= r2 < N and 0 <= c2 < M and not visited[r2][c2] and underground[r2][c2] in dic_pipe['up']:
                Q.append([r2, c2])
                visited[r2][c2] = visited[r][c] + 1
            # 좌
            r2 = r + dr[3]
            c2 = c + dc[3]
            if 0 <= r2 < N and 0 <= c2 < M and not visited[r2][c2] and underground[r2][c2] in dic_pipe['left']:
                Q.append([r2, c2])
                visited[r2][c2] = visited[r][c] + 1


for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1
    Escape(R, C)
    ans = 0
    for i in visited:
        for j in i:
            if 0 < j <= L:
                ans += 1
    print(f'#{tc}', ans)