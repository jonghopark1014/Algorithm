def dieFly(y, x, M):
    global sumV, maxV
    for r in range(y, y+M):
        for c in range(x, x+M):
            sumV += lst_N[r][c]
    if maxV < sumV:
        maxV = sumV
        sumV = 0
    else:
        sumV = 0

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst_N = [list(map(int, input().split())) for _ in range(N)]
    sumV = 0
    maxV = 0
    for r in range(N-M+1):
        for c in range(N-M+1):
            dieFly(r, c, M)

    print(f'#{tc} {maxV}')