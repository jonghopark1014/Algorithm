T = int(input())

def incoder(v):
    global l, r
    if v <= N:
        incoder(v * 2)
        incoder(v * 2 + 1)
        if not tree[v]:
            if v * 2 + 1 > N:
                tree[v] = tree[v * 2]
            else:
                tree[v] = tree[v * 2] + tree[v * 2 + 1]


for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for i in range(M):
        a, b = map(int, input().split())
        tree[a] = b
    l, r = 0, 0
    incoder(1)
    print(f'#{tc}', tree[L])