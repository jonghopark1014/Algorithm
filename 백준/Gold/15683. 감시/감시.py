import sys

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def Undo(r, c, dir):
    dir_lst = list(dir)
    for i in dir_lst:
        r2 = r + dr[int(i)]
        c2 = c + dc[int(i)]
        if 0 <= r2 < N and 0 <= c2 < M and lst_map[r2][c2] != 6:
            visited[r2][c2] -=1
            while True:
                r2 += dr[int(i)]
                c2 += dc[int(i)]
                if 0 <= r2 < N and 0 <= c2 < M:
                    if lst_map[r2][c2] == 6:
                        break
                    else:
                        visited[r2][c2] -= 1
                else:
                    break


def Install(r, c, dir):
    dir_lst = list(dir)
    for i in dir_lst:
        r2 = r + dr[int(i)]
        c2 = c + dc[int(i)]
        if 0 <= r2 < N and 0 <= c2 < M and lst_map[r2][c2] != 6:
            visited[r2][c2] += 1
            while True:
                r2 += dr[int(i)]
                c2 += dc[int(i)]
                if 0 <= r2 < N and 0 <= c2 < M:
                    if lst_map[r2][c2] == 6:
                        break
                    else:
                        visited[r2][c2] += 1
                else:
                    break

def dfs(cam_num):
    global ans
    if cam_num == len(cam_lst):
        tmp_ans = 0
        for i in visited:
            tmp_ans += i.count(0)
        ans = min(ans, tmp_ans)
        return
    r, c = cam_lst[cam_num]
    visited[r][c] += 1
    if lst_map[r][c] == 1:
        for i in range(4):
            dir = str(i)
            Install(r, c, dir)
            dfs(cam_num + 1)
            Undo(r, c, dir)
    elif lst_map[r][c] == 2:
        for i in range(2):
            dir = str(i)
            dir += str((i + 2) % 4)
            Install(r, c, dir)
            dfs(cam_num + 1)
            Undo(r, c, dir)
    elif lst_map[r][c] == 3:
        for i in range(4):
            dir = str(i)
            dir += str((i + 1) % 4)
            Install(r, c, dir)
            dfs(cam_num + 1)
            Undo(r, c, dir)
    elif lst_map[r][c] == 4:
        for i in range(4):
            dir = str(i)
            dir += str((i + 1) % 4)
            dir += str((i + 2) % 4)
            Install(r, c, dir)
            dfs(cam_num + 1)
            Undo(r, c, dir)
    elif lst_map[r][c] == 5:
        Install(r, c, '0123')
        dfs(cam_num + 1)
        Undo(r, c, '0123')


N, M = map(int, sys.stdin.readline().split())
lst_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cam_lst = []
wall_lst = []

for r in range(N):
    for c in range(M):
        if 1 <= lst_map[r][c] < 6:
            cam_lst.append([r, c])
        elif lst_map[r][c] == 6:
            wall_lst.append([r, c])

visited = [[0] * M for _ in range(N)]
for i in wall_lst:
    visited[i[0]][i[1]] = 10
ans = N * M
dfs(0)

print(ans)
