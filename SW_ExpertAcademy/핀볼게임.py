from collections import deque

T = int(input())

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

dir_dic = {
    1:[1, 3, 0, 2], 2:[1, 2, 3, 0], 3:[2, 0, 3, 1], 4:[3, 0, 1, 2],
    5:[1, 0, 3, 2]
}

def bfs(idx):
    global ans
    idx = idx
    while True:
        idx += 1
        if idx == len(zero_lst):
            break
        else:
            r, c = zero_lst[idx]
            start_r, start_c = r, c
            Q = deque()
            for i in range(4):
                Q.append([r, c, i, 0])

            while Q:
                r, c, direct, cnt =Q.popleft()
                r2 = r + dr[direct]
                c2 = c + dc[direct]
                if 0 <= r2 < N and 0 <= c2 < N:
                    if 1 <= lst_N[r2][c2] <= 5:
                        Q.append([r2, c2, dir_dic[lst_N[r2][c2]][direct], cnt + 1])
                    elif 6 <= lst_N[r2][c2] <= 10:
                        idx2 = 99
                        for i in range(2):
                            if hall_lst[lst_N[r2][c2]][i] == [r2, c2]:
                                idx2 = (i + 1) % 2
                        Q.append([hall_lst[lst_N[r2][c2]][idx2][0], hall_lst[lst_N[r2][c2]][idx2][1], direct, cnt])
                    elif lst_N[r2][c2] == -1 or (r2 == start_r and c2 == start_c):
                        ans = max(ans, cnt)
                    elif lst_N[r2][c2] == 0:
                        Q.append([r2, c2, direct, cnt])
                elif r2 < 0:
                    Q.append([r2, c2, 2, cnt + 1])
                elif r2 > N - 1:
                    Q.append([r2, c2, 3, cnt + 1])
                elif c2 < 0:
                    Q.append([r2, c2, 0, cnt + 1])
                elif c2 > N - 1:
                    Q.append([r2, c2, 1, cnt + 1])

ans_lst = []
for tc in range(1, T+1):
    N = int(input())

    lst_N = [list(map(int, input().split())) for _ in range(N)]

    hall_lst = [[] for _ in range(11)]
    zero_lst = []
    ans = 0

    for r in range(N):
        for c in range(N):
            if 6 <= lst_N[r][c] <= 10:
                hall_lst[lst_N[r][c]].append([r, c])
            elif lst_N[r][c] == 0:
                zero_lst.append([r, c])

    bfs(-1)
    ans_lst.append(f'#{tc} {ans}')

print('\n'.join(ans_lst))