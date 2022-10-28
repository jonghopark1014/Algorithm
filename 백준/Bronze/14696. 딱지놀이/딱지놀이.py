import sys

N = int(sys.stdin.readline())
for i in range(N):
    A = list(map(int, sys.stdin.readline().split()))
    count_A = [0] * 5
    for i in A[1:]:
        count_A[i] += 1

    B = list(map(int, sys.stdin.readline().split()))
    count_B = [0] * 5
    for i in B[1:]:
        count_B[i] += 1

    for i in range(4, 0, -1):
        if count_A[i] > count_B[i]:
            print('A')
            break
        elif count_A[i] < count_B[i]:
            print('B')
            break
    else:
        print('D')