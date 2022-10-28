T = int(input())

def solve(x):
    global N, num
    if x <= N:
        solve(x * 2)
        lst_N[x] = num
        num += 1
        solve(x * 2 + 1)

for tc in range(1, T+1):
    N = int(input())
    lst_N = [0] * (N + 1)
    num = 1
    solve(1)

    print(f'#{tc} {lst_N[1]} {lst_N[N//2]}')