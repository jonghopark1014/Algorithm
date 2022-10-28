import sys

def binary(set1, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if set1[mid] == target:
            return 1
        elif set1[mid] < target:
            start = mid +1
        elif set1[mid] > target:
            end = mid -1
    return 0


N, M = map(int, sys.stdin.readline().split())
lst_N = sorted([sys.stdin.readline().rstrip() for _ in range(N)])
lst_M = [sys.stdin.readline().rstrip() for _ in range(M)]
cnt = 0

for i in range(len(lst_M)):
    cnt += binary(lst_N, lst_M[i], 0, N-1)

print(cnt)