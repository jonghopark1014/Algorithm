import sys

def binary(lst, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if lst[mid] == target:
            return 1
        elif lst[mid] > target:
            end = mid - 1
        elif lst[mid] < target:
            start = mid + 1
    return 0

A = int(sys.stdin.readline())
lst_A = sorted(list(map(int, sys.stdin.readline().split())))
B = int(sys.stdin.readline())
lst_B = list(map(int, sys.stdin.readline().split()))

for i in range(len(lst_B)):
    print(binary(lst_A, lst_B[i], 0, A-1), end = ' ')