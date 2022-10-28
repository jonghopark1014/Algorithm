for tc in range(1, int(input()) + 1):
    N = int(input())
    lst_x = list(map(int, input().split()))
    lst_y = list(map(int, input().split()))
    E = float(input())
    weigh_lst = []
    for r in range(N):
        for c in range(r+1, N):
            weigh_lst.append([(E * ((lst_x[r] - lst_x[c]) ** 2 + (lst_y[r] - lst_y[c]) ** 2)), r, c])
    weigh_lst.sort()
    check_lst = [i for i in range(N)]

    s = 0
    for i in range(len(weigh_lst)):
        if check_lst[weigh_lst[i][1]] != check_lst[weigh_lst[i][2]]:
            s += weigh_lst[i][0]
            if check_lst[weigh_lst[i][1]] > check_lst[weigh_lst[i][2]]:
                value = check_lst[weigh_lst[i][2]]
                value2 = check_lst[weigh_lst[i][1]]
                for j in range(N):
                    if check_lst[j] == value2:
                        check_lst[j] = value
            else:
                value = check_lst[weigh_lst[i][1]]
                value2 = check_lst[weigh_lst[i][2]]
                for j in range(N):
                    if check_lst[j] == value2:
                        check_lst[j] = value
    print(f'#{tc}', round(s))