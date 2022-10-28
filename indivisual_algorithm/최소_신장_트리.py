def prim(x):
    MST = [0] * (V + 1)
    MST[x] = 1
    sum_w = 0

    for i in range(V):
        u = 0
        min_v = 10000000
        for j in range(V+1):
            if MST[j] == 1:
                for k in range(V+1):
                    if G[j][k] != 0 and MST[k] == 0 and min_v > G[j][k]:
                        u = k
                        min_v = G[j][k]
        sum_w += min_v
        MST[u] = 1
    return sum_w

ans_lst = []

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    G = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        u, v, weight = map(int, input().split())
        G[u][v] = weight
        G[v][u] = weight
    ans_lst.append(f'#{tc} {prim(0)}')

print('\n'.join(ans_lst))
