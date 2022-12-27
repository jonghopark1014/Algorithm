N, K = map(int, input().split())

arr_N = [0 for _ in range(N)]
res = 0

for i in range(N-1, -1, -1):
    tmp = int(input())
    arr_N[i] = tmp

idx = -1

while True:
    if K == 0:
        break
    for i in range(idx + 1, N):
        if arr_N[i] <= K:
            idx = i
            need_coin = K // arr_N[i]
            res += need_coin
            K -= arr_N[i] * need_coin
            break

print(res)