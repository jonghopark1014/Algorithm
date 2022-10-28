import sys

N, M = map(int, sys.stdin.readline().split())

lst_N = list(map(int, sys.stdin.readline().split()))

left = 0
right = max(lst_N) -1

while left <= right:
    mid = (left+right) // 2
    cnt_total = 0
    for i in lst_N:
        if i-mid > 0:
            cnt_total += i - mid
            if cnt_total > M:  
                break
    if cnt_total >= M:
        left = mid + 1
    elif cnt_total < M:
        right = mid - 1

print(right)