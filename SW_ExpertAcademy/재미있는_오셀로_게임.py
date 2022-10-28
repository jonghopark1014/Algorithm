T = int(input())

dr = [1, -1, 0, 0, 1, -1, 1, -1]
dc = [0, 0, 1, -1, 1, -1, -1, 1]

def Othello(r, c, color):
    for i in range(8):
        ans = 0
        while True:
            ans += 1
            r += dr[i]
            c += dc[i]
            if r < 0 or c < 0 or r > N-1 or c > N-1:
                for j in range(ans):
                    r -= dr[i]
                    c -= dc[i]
                break
            if board[r][c] == 0:
                for j in range(ans):
                    r -= dr[i]
                    c -= dc[i]
                break
            elif board[r][c] == color:
                for j in range(ans):
                    r -= dr[i]
                    c -= dc[i]
                    board[r][c] = color
                break


for tc in range(1, T+1):
    # N * N 판 & M 개의 횟수
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1] = 2
    board[N // 2 - 1][N // 2] = 1
    board[N // 2][N // 2 - 1] = 1
    board[N // 2][N // 2] = 2
    for _ in range(M):
        x, y, color = map(int, input().split())
        x -= 1
        y -= 1
        board[x][y] = color
        Othello(x, y, color)

    black = 0
    white = 0
    for r in board:
        black += r.count(1)
        white += r.count(2)
    print(f'#{tc}', black, white)