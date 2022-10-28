import sys

N = int(sys.stdin.readline())
tmp_lst = []
for i in range(N):
    a, b = list(map(int, sys.stdin.readline().split()))
    for j in range(10):
        for k in range(10):
            if [a+j,b+k] not in tmp_lst:
                tmp_lst.append([a+j,b+k])

print(len(tmp_lst))