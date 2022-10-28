import sys

T = int(sys.stdin.readline())

for tc in range(1, T+1):
    X, Y = 1, 1
    H, W, N = map(int, sys.stdin.readline().split())
    p_cnt = 1
    if N != 1:

        while True:
            if Y >= H:
                X += 1
                Y = 1
            else:
                Y += 1
            p_cnt += 1
            if p_cnt == N:
                break
    print(100*Y + X)