T = int(input())

def Bomb(r, c, size):
    global N, result
    i, j, k, l = r - size, r + size, c - size, c + size
    if i < 0:
        i = 0
    if j > N-1:
        j = N-1
    if k < 0:
        k = 0
    if l > N-1:
        l = N-1

    for a in range(i, j+1):
        if [a, c] not in comp_M:
            comp_M.append([a, c])
            result += lst_N[a][c]
    for b in range(k, l+1):
        if [r, b] not in comp_M:
            comp_M.append([r, b])
            result += lst_N[r][b]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst_N = [list(map(int, input().split())) for _ in range(N)]
    lst_M = [list(map(int, input().split())) for _ in range(M)]
    comp_M = []
    result = 0
    for i in lst_M:
        Bomb(i[0], i[1], i[2])

    print(f'#{tc} {result}')