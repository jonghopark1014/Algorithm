import sys

N, M = map(int, sys.stdin.readline().split())
lst_N = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
K = int(sys.stdin.readline())
lst_K = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

for i in range(len(lst_N)):
    sumV = 0
    for j in range(len(lst_N[i])):
        sumV += lst_N[i][j]
        lst_N[i][j] = sumV
    lst_N[i].insert(0, 0)

for i in lst_K:
    if i[2] - i[0] == N-1 and i[3] - i[1] == M-1:
        value = 0
        for j in lst_N:
            value += j[-1]
        print(value)
    elif i[3] == i[1]:
        value = 0
        for a in range(i[0]-1, i[2]):
            value += lst_N[a][i[3]] - lst_N[a][i[3]-1]
        print(value)
    else:
        value = 0
        for a in range(i[0]-1, i[2]):
            value += lst_N[a][i[3]] - lst_N[a][i[1]-1]
        print(value)
