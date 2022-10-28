import sys
from itertools import combinations
from heapq import heappush
import copy

dr = [-1, -1, -1]
dc = [-1, 0, 1]

N, M, D = map(int, sys.stdin.readline().split())

archer_lst = list(combinations(range(M), 3))

lst_basic = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lst_basic = lst_basic + [[0] * M]
ans = 0

for i in archer_lst:
    lst_N = copy.deepcopy(lst_basic)
    a1, a2, a3 = i
    tmp_archer = [[N, a1], [N, a2], [N, a3]]
    tmp_cnt = 0
    while True:
        tmp_one_lst2 = []
        for r in range(N):
            for c in range(M):
                if lst_N[r][c] == 1:
                    tmp_one_lst2.append([r,c])
        if len(tmp_one_lst2) == 0:
            ans = max(tmp_cnt, ans)
            break
        else:
            for i in range(3):
                r, c = tmp_archer[i]
                tmp_target = []
                for j in tmp_one_lst2:
                    r2, c2 = j
                    value = abs(r2 - r) + abs(c2 - c)
                    if value <= D:
                        heappush(tmp_target, [value, c2, r2])

                if tmp_target:
                    value, c3, r3 = tmp_target[0]
                    lst_N[r3][c3] += 1

            for r in range(N):
                for c in range(M):
                    if lst_N[r][c] != 0 and lst_N[r][c] != 1:
                        tmp_cnt += 1
                        lst_N[r][c] = 0

            tmp_one_lst = []
            for r in range(N):
                for c in range(M):
                    if lst_N[r][c] == 1:
                        tmp_one_lst.append([r, c])

            for i in tmp_one_lst:
                r, c = i
                if r != N - 1:
                    lst_N[r][c] -= 1
                    lst_N[r+1][c] += 1
                else:
                    lst_N[r][c] -= 1

print(ans)