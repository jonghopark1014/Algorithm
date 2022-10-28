T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst_N = [list(map(int, input().split())) for _ in range(N)]
    lst_M = [list(map(int, input().split())) for _ in range(M)]
    tmp_lst = []
    result = 0
    for i in lst_M:
        for r in range(i[1], i[1]+i[2]):
            for c in range(i[0], i[0] + i[2]):
                if r > N-1 or c > N-1:
                    break
                if [c,r] not in tmp_lst:
                    tmp_lst += [[c,r]]
                    result += lst_N[c][r]
    print(f'#{tc} {result}')