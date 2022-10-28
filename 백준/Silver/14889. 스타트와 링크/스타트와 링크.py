import sys
from itertools import combinations

N = int(sys.stdin.readline())

lst_N = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

num_n = set(i for i in range(N))
combi = list(combinations(num_n, N // 2))
ans = 999999999

for i in combi:
    comp_set = num_n - set(i)
    i = list(i)
    comp_set = list(comp_set)
    combi_sum, comp_sum = 0, 0

    for idx in range(N // 2):
        for idx2 in range(N // 2):
            if idx != idx2:
                combi_sum += lst_N[i[idx]][i[idx2]]
                comp_sum += lst_N[comp_set[idx]][comp_set[idx2]]

    ans = min(abs(combi_sum - comp_sum), ans)

print(ans)