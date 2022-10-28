import sys

N = int(sys.stdin.readline())
tmp_lst = [[0] * 1001 for _ in range(1001)]

for i in range(1, N+1):
    a, b, c, d = map(int, sys.stdin.readline().split())
    for j in range(b, b+d):
        for k in range(a, a+c):
            tmp_lst[j][k] = i

for a in range(1, N+1):
    cnt = 0
    for b in range(1001):
        cnt += tmp_lst[b].count(a)
    print(cnt)