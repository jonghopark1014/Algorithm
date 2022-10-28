T = int(input())

def incoder(value):
    global ans
    if value == 0:
        return
    ans += 1
    incoder(L[value])
    incoder(R[value])


for tc in range(1, T+1):
    E, N = map(int, input().split())
    V = E + 1
    L = [0] * (V+1)
    R = [0] * (V+1)
    P = [0] * (V+1)
    lst_E = list(map(int, input().split()))
    for i in range(0, len(lst_E), 2):
        if L[lst_E[i]] == 0:
            L[lst_E[i]] = lst_E[i + 1]
        else:
            R[lst_E[i]] = lst_E[i + 1]
        P[lst_E[i + 1]] = lst_E[i]
    ans = 0
    incoder(N)
    print(f'#{tc} {ans}')