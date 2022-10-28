import sys

N = int(sys.stdin.readline())

lst_N = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt_lst = []
cnt = 1

for i in range(len(lst_N)):
    for j in range(len(lst_N)):
        if lst_N[i][0] < lst_N[j][0] and lst_N[i][1] < lst_N[j][1]:
            cnt += 1
    cnt_lst += [cnt]
    cnt = 1

print(*cnt_lst)