import sys

N = int(sys.stdin.readline())

lst_N = list(map(int, sys.stdin.readline().split()))

re_N = sorted(list(set(lst_N)))
dic_N = {}
for idx, value in enumerate(re_N):
    dic_N[value] = idx

for i in range(len(lst_N)):
    lst_N[i] = dic_N[lst_N[i]]

print(*lst_N)