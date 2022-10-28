T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst_N = [list(map(int, list(input()))) for _ in range(N)]
    mid = r = N // 2
    result = sum(lst_N[mid])
    a = 0
    while True:
        r -= 1
        a += 1
        if r == -1:
            break
        for i in range(0+a, N-a):
            result += lst_N[r][i]
            result += lst_N[N-r-1][i]

    print(f'#{tc} {result}')
