def MST():
    s = 0
    for i in range(E):
        if check_lst[G[i][0]] != check_lst[G[i][1]]:
            s += G[i][2]
            if check_lst[G[i][0]] > check_lst[G[i][1]]:
                value = check_lst[G[i][0]]
                for j in range(V+1):
                    if check_lst[j] == value:
                        check_lst[j] = check_lst[G[i][1]]
            else:
                value = check_lst[G[i][1]]
                for j in range(V+1):
                    if check_lst[j] == value:
                        check_lst[j] = check_lst[G[i][0]]

    return s

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    G = []
    for i in range(E):
        p, c, w = map(int, input().split())
        G.append((p, c, w))
    G.sort(key= lambda x: x[2])
    check_lst = [i for i in range(V+1)]
    print(f'#{tc} {MST()}')

