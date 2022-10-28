def maze(y, x):
    global result
    if y == y2 and x == x2:
        result = 1
    elif lst_N[y][x] == '0':
        lst_N[y][x] = '1'
        if y-1 > 0:
            if lst_N[y-1][x] == '0':
                maze(y-1, x)
        if y+1 < 16:
            if lst_N[y+1][x] == '0':
                maze(y+1, x)
        if x - 1 > 0:
            if lst_N[y][x-1] == '0':
                maze(y, x-1)
        if x + 1 < 16:
            if lst_N[y][x+1] == '0':
                maze(y, x+1)
        lst_N[y][x] = '0'

for _ in range(10):
    tc = int(input())
    lst_N = [list(input()) for _ in range(16)]
    result = 0
    for i in range(len(lst_N)):
        for j in range(len(lst_N)):
            if lst_N[i][j] == '2':
                x1, y1 = j, i
                lst_N[i][j] = '0'
            if lst_N[i][j] == '3':
                x2, y2 = j, i
                lst_N[i][j] = '0'
    maze(y1, x1)
    print(f'#{tc} {result}')