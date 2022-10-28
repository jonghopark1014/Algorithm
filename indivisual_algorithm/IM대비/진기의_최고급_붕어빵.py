T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst_N = list(map(int, input().split()))
    bread = 0
    for i in range(0, max(lst_N)+1):
        if i == 0:
            if i in lst_N:
                print(f'#{tc} Impossible')
                break
        else:
            if i % M == 0:
                bread += K
            if i in lst_N:
                a = lst_N.count(i)
                bread -= (1 * a)
                if bread < 0:
                    print(f'#{tc} Impossible')
                    break
    else:
        print(f'#{tc} Possible')