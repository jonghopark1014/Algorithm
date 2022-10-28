import sys

N = int(sys.stdin.readline())
lst_N = sorted([list(sys.stdin.readline().split()) + [_] for _ in range(N)], key = lambda x:(int(x[0]), x[2]))
for i in lst_N:
    print(*i[:2])
