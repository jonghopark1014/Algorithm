T = int(input())

for tc in range(1, T+1):
    N = list(input())
    cnt = 0
    while True:
        cnt += 1
        a = N.index('1')
        for i in range(a, len(N)):
            if N[i] == '1':
                N[i] = '0'
            else:
                N[i] = '1'
        if N == ['0'] * len(N):
            break
    print(f'#{tc} {cnt}')