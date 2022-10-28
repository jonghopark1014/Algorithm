import sys

N = int(sys.stdin.readline())

# dir 1 가로 2 세로 3 대각선

def makePipe(r, c, direct):
    global ans
    if r == N - 1 and c == N - 1:
        ans += 1
        return
    else:
        if c + 1 < N and lst_N[r][c + 1] != 1:
            if direct == 1 or direct == 3:
                lst_N[r][c+1] = 9
                makePipe(r, c + 1, 1)
                lst_N[r][c + 1] = 0

        if r + 1 < N and c + 1 < N and lst_N[r + 1][c + 1] != 1:
            if lst_N[r+1][c] == 0 and lst_N[r][c + 1] == 0:
                lst_N[r+1][c+1] = 9
                makePipe(r + 1, c + 1, 3)
                lst_N[r + 1][c + 1] = 0

        if r + 1 < N and lst_N[r + 1][c] != 1:
            if direct == 2 or direct == 3:
                lst_N[r + 1][c] = 9
                makePipe(r+1, c, 2)
                lst_N[r + 1][c] = 0

lst_N = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

if lst_N[N-1][N-1] != 1:
    lst_N[0][0], lst_N[0][1] = 9, 9
    ans = 0

    makePipe(0, 1, 1)
    print(ans)
else:
    print(0)
