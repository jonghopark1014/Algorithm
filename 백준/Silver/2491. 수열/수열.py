import sys

N = int(sys.stdin.readline())
lst_N = list(map(int, sys.stdin.readline().split()))

max_cnt = 1
cnt_a = 1
cnt_b = 1

for i in range(N-1):
    if lst_N[i] < lst_N[i+1]:
        cnt_a += 1
        cnt_b = 1
    elif lst_N[i] > lst_N[i+1]:
        cnt_a = 1
        cnt_b += 1
    else:
        cnt_a += 1
        cnt_b += 1
    if cnt_a > cnt_b:
        cnt = cnt_a
    else:
        cnt = cnt_b
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)