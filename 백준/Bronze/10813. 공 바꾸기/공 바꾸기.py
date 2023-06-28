import sys

ss = sys.stdin.readline

N, M = map(int, ss().split())

arr = [i for i in range(1, N + 1)]

for i in range(M):
    a, b = map(int, ss().split())
    arr[a - 1], arr[b - 1] = arr[b - 1], arr[a - 1]

print(*arr)


