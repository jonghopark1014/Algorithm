import sys

R, C = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
stage = [[0 for _ in range(R)] for _ in range(C)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dist = 0
n_col = n_row = 0
if K > C * R:
    print(0)
else:
    for i in range(1, C*R+1):
        stage[n_col][n_row] = i
        if i == K:
            result = [n_row+1, n_col+1]
        n_col += dc[dist]
        n_row += dr[dist]
        if 0 > n_col or n_col > C-1 or 0 > n_row or n_row > R-1 or stage[n_col][n_row] != 0:
            n_col -= dc[dist]
            n_row -= dr[dist]
            dist = (dist+1) % 4

            n_col += dc[dist]
            n_row += dr[dist]

    print(result[0], result[1])