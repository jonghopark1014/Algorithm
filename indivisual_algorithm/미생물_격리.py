from collections import deque

T = int(input())

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

ans_lst = []
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst_N = [[[] for _ in range(N)] for _ in range(N)]
    Q = deque()
    # 상 1 하 2 좌 3 우 4
    for i in range(K):
        r, c, cell, direc = map(int, input().split())
        lst_N[r][c] = [[cell, direc]]
        Q.append([r, c, cell, direc])
    for i in range(M):
        if i != M - 1:
            while Q:
                r, c, cell, direc = Q.popleft()
                r2 = r + dr[direc]
                c2 = c + dc[direc]
                if r2 == 0 or c2 == 0 or r2 == N-1 or c2 == N-1:
                        if direc == 1:
                            direc = 2
                        elif direc == 2:
                            direc = 1
                        elif direc == 3:
                            direc = 4
                        elif direc == 4:
                            direc = 3
                        cell = cell // 2
                        if cell != 0:
                            lst_N[r2][c2].append([cell, direc])
                            lst_N[r][c].pop(0)
                        else:
                            lst_N[r][c].pop(0)
                else:
                    lst_N[r2][c2].append([cell, direc])
                    lst_N[r][c].pop(0)
            for r in range(N):
                for c in range(N):
                    if len(lst_N[r][c]) > 1:
                        cell = 0
                        direct = 0
                        max_cell = 0
                        for i in range(len(lst_N[r][c])):
                            if i == 0:
                                cell += lst_N[r][c][i][0]
                                max_cell = lst_N[r][c][i][0]
                                direct = lst_N[r][c][i][1]
                            else:
                                cell += lst_N[r][c][i][0]
                                if max_cell < lst_N[r][c][i][0]:
                                    max_cell = lst_N[r][c][i][0]
                                    direct = lst_N[r][c][i][1]
                        lst_N[r][c] = [[cell, direct]]
                        Q.append([r, c, cell, direct])
                    elif len(lst_N[r][c]) == 1:
                        Q.append([r, c, lst_N[r][c][0][0], lst_N[r][c][0][1]])
        elif i == M - 1:
            ans = 0
            while Q:
                r, c, cell, direc = Q.popleft()
                r2 = r + dr[direc]
                c2 = c + dc[direc]
                if r2 == 0 or c2 == 0 or r2 == N-1 or c2 == N-1:
                        if direc == 1:
                            direc = 2
                        elif direc == 2:
                            direc = 1
                        elif direc == 3:
                            direc = 4
                        elif direc == 4:
                            direc = 3
                        cell = cell // 2
                        if cell != 0:
                            lst_N[r2][c2].append([cell, direc])
                            lst_N[r][c].pop(0)
                        else:
                            lst_N[r][c].pop(0)
                else:
                    lst_N[r2][c2].append([cell, direc])
                    lst_N[r][c].pop(0)
            for r in range(N):
                for c in range(N):
                    if len(lst_N[r][c]) > 1:
                        cell = 0
                        direct = 0
                        max_cell = 0
                        for i in range(len(lst_N[r][c])):
                            if i == 0:
                                cell += lst_N[r][c][i][0]
                                max_cell = lst_N[r][c][i][0]
                                direct = lst_N[r][c][i][1]
                            else:
                                cell += lst_N[r][c][i][0]
                                if max_cell < lst_N[r][c][i][0]:
                                    max_cell = lst_N[r][c][i][0]
                                    direct = lst_N[r][c][i][1]
                        lst_N[r][c] = [[cell, direct]]
                        ans += cell
                    elif len(lst_N[r][c]) == 1:
                        ans += lst_N[r][c][0][0]

    ans_lst.append(f'#{tc} {ans}')
print('\n'.join(ans_lst))