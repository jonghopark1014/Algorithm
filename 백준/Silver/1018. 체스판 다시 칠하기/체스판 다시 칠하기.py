import sys

N, M = map(int, sys.stdin.readline().split())

lst_N = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

WB = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']
BW = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']

# WB 먼저

ans = 99999

for r1 in range(0, N-8+1):
    for c1 in range(0, M-8+1):
        cnt = 0
        for r2 in range(0, 8, 2):
            for c2 in range(8):
                if lst_N[r1+r2][c1+c2] != WB[c2]:
                    cnt += 1
        for r3 in range(1, 8, 2):
            for c3 in range(8):
                if lst_N[r1+r3][c1+c3] != BW[c3]:
                    cnt += 1
        if cnt < ans:
            ans = cnt

for r1 in range(0, N-8+1):
    for c1 in range(0, M-8+1):
        cnt = 0
        for r2 in range(0, 8, 2):
            for c2 in range(0, 8):
                if lst_N[r1+r2][c1+c2] != BW[c2]:
                    cnt += 1
        for r3 in range(1, 8, 2):
            for c3 in range(0, 8):
                if lst_N[r1+r3][c1+c3] != WB[c3]:
                    cnt += 1
        if cnt < ans:
            ans = cnt

print(ans)