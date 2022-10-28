import sys

x, y = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
lst_zero = [0, y]
lst_one = [0, x]
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if a == 0:
        lst_zero += [b]
    else:
        lst_one += [b]

lst_zero.sort()
lst_one.sort()
re_zero = [lst_zero[j] - lst_zero[j - 1] for j in range(1, len(lst_zero))]
re_one = [lst_one[j] - lst_one[j - 1] for j in range(1, len(lst_one))]

maxV = 0
compV = 0
for i in re_zero:
    for j in re_one:
        compV = i * j
        if compV > maxV:
            maxV = compV
    compV = 0

print(maxV)