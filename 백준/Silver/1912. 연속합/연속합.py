import sys

n = int(sys.stdin.readline())
lst_N = list(map(int, input().split()))

max_v = lst_N[0]
for i in range(1, n):
    lst_N[i] = max(lst_N[i], lst_N[i] + lst_N[i-1])
    max_v = max(max_v, lst_N[i])
print(max_v)

