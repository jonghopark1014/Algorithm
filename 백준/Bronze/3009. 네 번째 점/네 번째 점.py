import sys

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
C = list(map(int, sys.stdin.readline().split()))

value_x = 0
value_y = 0

if A[0] - B[0] != 0:
    if A[0] - C[0] != 0:
        value_x = A[0]
    else:
        value_x = B[0]
else:
    value_x = C[0]

if A[1] - B[1] != 0:
    if A[1] - C[1] != 0:
        value_y = A[1]
    else:
        value_y = B[1]
else:
    value_y = C[1]

print(value_x, value_y)