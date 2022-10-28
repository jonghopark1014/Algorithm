def maze(y, x):
    global cnt, N, result
    if y == y2 and x == x2:
        result.append(cnt)
    elif lst_N[y][x] == '0':
        lst_N[y][x] = '1'
        cnt += 1
        if y-1 > -1:
            if lst_N[y-1][x] == '0':
                maze(y-1, x)
        if y+1 < N:
            if lst_N[y+1][x] == '0':
                maze(y+1, x)
        if x - 1 > -1:
            if lst_N[y][x-1] == '0':
                maze(y, x-1)
        if x + 1 < N:
            if lst_N[y][x+1] == '0':
                maze(y, x+1)
        lst_N[y][x] = '0'
        cnt -= 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst_N = [list(input()) for _ in range(N)]
    cnt = 0
    result = []
    for i in range(len(lst_N)):
        for j in range(len(lst_N)):
            if lst_N[i][j] == '2':
                x1, y1 = j, i
                lst_N[i][j] = '0'
            if lst_N[i][j] == '3':
                x2, y2 = j, i
                lst_N[i][j] = '0'
    maze(y1, x1)
    if len(result) != 0:
        a = min(result)
        print(f'#{tc} {a - 1}')
    else:
        print(f'#{tc} 0')