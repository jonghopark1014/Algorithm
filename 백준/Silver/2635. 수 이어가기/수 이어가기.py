import sys

N = int(sys.stdin.readline())
max_cnt = 0
max_lst = []
if N == 0:
    print(0)
    print(0)
else:
    for i in range(N//2+1, N+1):
        sum_lst = [N, i]
        b = 0
        while sum_lst[b] - sum_lst[b+1] >= 0:
            sum_lst.append(sum_lst[b]-sum_lst[b+1])
            b += 1
        if max_cnt < len(sum_lst):
            max_cnt = len(sum_lst)
            max_lst = sum_lst

    print(max_cnt)
    print(*max_lst)