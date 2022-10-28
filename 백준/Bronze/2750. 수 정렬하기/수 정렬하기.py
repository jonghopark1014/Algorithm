import sys

N = int(sys.stdin.readline())
lst_N = [int(sys.stdin.readline()) for _ in range(N)]
lst_N = list(set(lst_N))
for i in sorted(lst_N):
    print(i)