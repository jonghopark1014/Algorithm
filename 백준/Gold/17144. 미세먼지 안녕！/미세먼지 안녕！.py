import sys

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

dr2 = [0, -1, 0, 1]
dc2 = [1, 0, -1, 0]

dr3 = [0, 1, 0, -1]
dc3 = [1, 0, -1, 0]

def Spread(lst):
    tmp_lst = [[0] * C for _ in range(R)]
    tmp_lst[air_lst[0][0]][air_lst[0][1]] = -1
    tmp_lst[air_lst[1][0]][air_lst[1][1]] = -1
    for i in lst:
        r, c = i[0], i[1]
        tmp_value = lst_map[r][c]
        for i in range(5):
            if i != 4:
                r2 = r + dr[i]
                c2 = c + dc[i]
                if 0 <= r2 < R and 0 <= c2 < C and tmp_lst[r2][c2] != -1:
                    tmp_value -= lst_map[r][c] // 5
                    tmp_lst[r2][c2] += lst_map[r][c] // 5
            else:
                r2 = r
                c2 = c
                tmp_lst[r2][c2] += tmp_value
    return tmp_lst

def fresh(lst):
    tmp_lst2 = [[0] * C for _ in range(R)]
    nr1 = air_lst[0][0]
    nc1 = air_lst[0][1]
    nr2 = air_lst[1][0]
    nc2 = air_lst[1][1]
    tmp_lst2[nr1][nc1] = -1
    tmp_lst2[nr2][nc2] = -1
    direc1 = 0
    direc2 = 0
    tmp_r1 = nr1 + dr2[direc1]
    tmp_c1 = nc1 + dc2[direc1]
    tmp_v1 = lst[tmp_r1][tmp_c1]
    tmp_r2 = nr2 + dr3[direc2]
    tmp_c2 = nc2 + dc3[direc2]
    tmp_v2 = lst[tmp_r2][tmp_c2]
    while True:
        tmp_r1 += dr2[direc1]
        tmp_c1 += dc2[direc1]
        if 0 <= tmp_r1 < R and 0 <= tmp_c1 < C:
            if lst[tmp_r1][tmp_c1] == -1:
                break
            tmp_lst2[tmp_r1][tmp_c1] = tmp_v1
            tmp_v1 = lst[tmp_r1][tmp_c1]
        else:
            tmp_r1 -= dr2[direc1]
            tmp_c1 -= dc2[direc1]
            direc1 += 1
    while True:
        tmp_r2 += dr3[direc2]
        tmp_c2 += dc3[direc2]
        if 0 <= tmp_r2 < R and 0 <= tmp_c2 < C:
            if lst[tmp_r2][tmp_c2] == -1:
                break
            tmp_lst2[tmp_r2][tmp_c2] = tmp_v2
            tmp_v2 = lst[tmp_r2][tmp_c2]
        else:
            tmp_r2 -= dr3[direc2]
            tmp_c2 -= dc3[direc2]
            direc2 += 1
    for r in range(1, nr1):
        for c in range(1, C - 1):
            if tmp_lst2[r][c] == 0:
                tmp_lst2[r][c] = lst[r][c]
    for r in range(nr2 + 1, R-1):
        for c in range(1, C - 1):
            if tmp_lst2[r][c] == 0:
                tmp_lst2[r][c] = lst[r][c]

    return tmp_lst2


R, C, T = map(int, sys.stdin.readline().split())
lst_map = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
comp_T = 0

while True:
    air_lst = []
    dust_lst = []
    comp_T += 1
    for r in range(R):
        for c in range(C):
            if lst_map[r][c] == -1:
                air_lst.append([r, c])
            elif lst_map[r][c] != 0:
                dust_lst.append([r, c])
    tmp_lst = Spread(dust_lst)
    lst_map = fresh(tmp_lst)
    if comp_T == T:
        ans = 0
        for r in lst_map:
            ans += sum(r)
        ans += 2
        break

print(ans)

