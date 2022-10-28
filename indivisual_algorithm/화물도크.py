T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst_se = sorted([list(map(int, input().split())) for _ in range(N)], key = lambda x : x[1])
    now = lst_se[0][1]
    ans = 1
    for i in lst_se:
        if i[0] >= now:
            ans += 1
            now = i[1]

    print(f'#{tc}', ans)