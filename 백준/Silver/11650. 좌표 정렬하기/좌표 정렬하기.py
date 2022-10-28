import sys

N = int(sys.stdin.readline())
lst_N = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

re_N = sorted(lst_N, key = lambda x:(x[0], x[1]))

for i in re_N:
    print(*i)