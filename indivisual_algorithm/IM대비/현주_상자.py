T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    lst_N = [0] * (N + 1)
    lst_Q = [0] + [list(map(int, input().split())) for _ in range(Q)]
    for i in range(1, len(lst_Q)):
        for j in range(lst_Q[i][0], lst_Q[i][1]+1):
            lst_N[j] = i
    print(f'#{tc}', *lst_N[1:])