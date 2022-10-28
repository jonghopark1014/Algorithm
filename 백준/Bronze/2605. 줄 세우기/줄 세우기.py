import sys

N = int(sys.stdin.readline())
lst_N = list(map(int, sys.stdin.readline().split()))
cnt_lst = [0] * N

for i in range(1, N+1):
    if cnt_lst[lst_N[i-1]] == 0:
        cnt_lst[lst_N[i-1]] = i
    else:
        cnt_lst.insert(lst_N[i-1], i)

print(*cnt_lst[0:N][::-1])