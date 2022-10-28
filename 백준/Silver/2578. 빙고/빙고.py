import sys

def bingo(lst):
    global lst_n, cnt, max_cnt
    acc = 0
    for i in lst_n:
        if i == [0, 0, 0, 0, 0]:
            acc += 1
            if acc == 3:
                max_cnt = cnt
                return
    tmp_lst = []
    for j in range(5):
        for k in range(5):
            tmp_lst += [lst_n[k][j]]
        if tmp_lst == [0, 0, 0, 0, 0]:
            acc += 1
            if acc == 3:
                max_cnt = cnt
                return
        tmp_lst = []
    tmp_lst2 = []
    for i in range(5):
        tmp_lst2 += [lst_n[0+i][0+i]]
    if tmp_lst2 == [0, 0, 0, 0, 0]:
        acc += 1
        if acc == 3:
            max_cnt = cnt
            return
    tmp_lst2 = []
    for i in range(5):
        tmp_lst2 += [lst_n[0+i][4-i]]
    if tmp_lst2 == [0, 0, 0, 0, 0]:
        acc += 1
        if acc == 3:
            max_cnt = cnt
            return
    return

cnt = 0
max_cnt = 0
lst_n = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

lst_a = []
for _ in range(5):
    lst_a += list(map(int, sys.stdin.readline().split()))

for i in lst_a:
    cnt += 1
    if cnt < 5:
        for j in lst_n:
            if i in j:
                j[j.index(i)] = 0
                break
    else:
        for j in lst_n:
            if i in j:
                j[j.index(i)] = 0
                break
        bingo(lst_n)
        if max_cnt:
            break

print(max_cnt)