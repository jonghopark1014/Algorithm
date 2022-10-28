import sys

N, K = map(int, sys.stdin.readline().split())
lst_p = list(map(int, sys.stdin.readline().split()))
lst_p.sort(reverse=True)
print(lst_p[K-1])