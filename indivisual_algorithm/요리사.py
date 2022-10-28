def dfs(level, cnt):
    global ans
    if cnt == N // 2:
        tmp_n = num_N - set(tmptmp1)
        tmp_n = list(tmp_n)
        tmp2.append(tmp_n)
        return
    for i in range(level + 1, N):
        tmptmp1.append(i)
        dfs(i, cnt + 1)
        tmptmp1.pop()



for tc in range(1, int(input()) + 1):
    N = int(input())
    lst_N = [list(map(int, input().split())) for _ in range(N)]
    ans = 999999999999
    num_N = set(i for i in range(N))
    tmptmp1 = [0]
    tmptmp2 = []
    tmp1 = []
    tmp2 = []
    dfs(0, 1)
    v1_lst = []
    v2_lst = []
    tmp_v1 = 0
    tmp_v2 = 0
    for i in tmp2:
        tmp_n = num_N - set(i)
        tmp_n = list(tmp_n)
        tmp1.append(tmp_n)
    for i in tmp1:
        for j in range(N // 2):
            for k in range(N // 2):
                if j != k:
                    tmp_v1 += lst_N[int(i[j])][int(i[k])]
        v1_lst.append(tmp_v1)
        tmp_v1 = 0
    for i in tmp2:
        for j in range(N // 2):
            for k in range(N // 2):
                if j != k:
                    tmp_v2 += lst_N[int(i[j])][int(i[k])]
        v2_lst.append(tmp_v2)
        tmp_v2 = 0
    for i in range(len(v1_lst)):
        ans = min(abs(v1_lst[i] - v2_lst[i]), ans)

    print(f'#{tc}', ans)