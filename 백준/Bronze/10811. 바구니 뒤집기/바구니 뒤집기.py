import sys

ssr = sys.stdin.readline

N, M = map(int, ssr().split())

arr = [i for i in range(1, N + 1)]

for i in range(M):
    a, b = map(int, ssr().split())
    for j in range((b - a) // 2 + 1):
        arr[a + j - 1], arr[b - j - 1] = arr[b - j - 1], arr[a + j - 1]

print(*arr)
