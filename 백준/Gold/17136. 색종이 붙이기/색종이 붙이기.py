import sys

dic_num = {
    1 : [[0, 0]],
    2 : [[0, 0], [0, 1], [1, 0], [1,1]],
    3 : [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]],
    4 : [[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 0], [3, 1], [3, 2], [3, 3]],
    5 : [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
}

def Install(lst, r, c, size):
    cnt = 0
    for i in lst:
        r2 = r + i[0]
        c2 = c + i[1]
        if 0 <= r2 < 10 and 0 <= c2 < 10 and  lst_N[r2][c2] == 1:
            cnt += 1
        else:
            return False
    if cnt == size:
        for i in lst:
            r2 = r + i[0]
            c2 = c + i[1]
            if 0 <= r2 < 10 and 0 <= c2 < 10 and lst_N[r2][c2] == 1:
                lst_N[r2][c2] = 9
        return True
    else:
        return False

def Undo(lst, r, c):
    for i in lst:
        r2 = r + i[0]
        c2 = c + i[1]
        if 0 <= r2 < 10 and 0 <= c2 < 10 and lst_N[r2][c2] == 9:
            lst_N[r2][c2] = 1
        else:
            return

def dfs(idx, one, two, thr, four, five):
    global ans
    if one + two + thr + four + five > ans:
        return
    if one > 5 or two > 5 or thr > 5 or four > 5 or five > 5:
        return
    if idx == len(one_lst):
        for lst in lst_N:
            if lst.count(1) != 0:
                return
        ans = min(ans, one + two + thr + four + five)
        return
    r, c = one_lst[idx]
    if lst_N[r][c] == 9:
        dfs(idx + 1, one, two, thr, four, five)
    else:
        for i in range(5, 0, -1):
            TF = Install(dic_num[i], r, c, i**2)
            if not TF:
                continue
            if i == 1:
                dfs(idx + 1, one + 1, two, thr, four, five)
            elif i == 2:
                dfs(idx + 1, one, two + 1, thr, four, five)
            elif i == 3:
                dfs(idx + 1, one, two, thr + 1, four, five)
            elif i == 4:
                dfs(idx + 1, one, two, thr, four + 1, five)
            elif i == 5:
                dfs(idx + 1, one, two, thr, four, five + 1)
            Undo(dic_num[i], r, c)




lst_N = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]

ans = 101

one_lst = []
for r in range(10):
    for c in range(10):
        if lst_N[r][c] == 1:
            one_lst.append([r, c])
if one_lst:
    dfs(0, 0, 0, 0, 0, 0)
else:
    ans = 0

if ans == 101:
    ans = -1

print(ans)
