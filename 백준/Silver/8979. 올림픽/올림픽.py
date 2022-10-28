import sys

N, K = map(int, sys.stdin.readline().split())

lst_N = [list(map(int, input().split())) + [_] for _ in range(N)]

lst_N.sort(key = lambda x:(x[0], x[1], x[2], x[3]))

for i in range(len(lst_N)):
    if lst_N[i][-1] == K-1:
        print(len(lst_N) - i)