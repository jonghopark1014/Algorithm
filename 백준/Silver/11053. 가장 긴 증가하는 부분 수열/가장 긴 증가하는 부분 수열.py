import sys

read_input = sys.stdin.readline

A = int(read_input())
arr = list(map(int, read_input().split()))
cnt = [1 for i in range(A)]

for i in range(1, A):
    for j in range(0, i):
        if arr[i] > arr[j]:
            cnt[i] = max(cnt[i], cnt[j] + 1)

print(max(cnt))
