N, M = map(int, input().split())

lst_A = [list(map(int, input().split())) for r in range(N)]
lst_B = [list(map(int, input().split())) for r in range(N)]

lst_C = [[] for _ in range(N)]

for r in range(N):
    for c in range(M):
        lst_C[r].append(lst_A[r][c] + lst_B[r][c])

for i in range(N):
    print(*lst_C[i])