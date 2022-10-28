import sys

K, N = map(int, sys.stdin.readline().split())
lst_K = [int(sys.stdin.readline()) for _ in range(K)]

left = 1
right = sum(lst_K) // N

while left <= right:
    cnt_mid = 0
    mid = (left + right) >> 1
    for i in lst_K:
        cnt_mid += i//mid
    if cnt_mid >= N:
        left = mid +1
    elif cnt_mid < N:
        right = mid -1

print(right)