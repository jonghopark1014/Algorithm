T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst_N = [list(input()) for _ in range(N)]
    result = 'NO'
    # 가로
    for i in lst_N:
        for j in range(N-5+1):
            cnt = 0
            for k in range(5):
                if i[j+k] == 'o':
                    cnt += 1
                if cnt == 5:
                    result = 'YES'
                    break

    # 세로
    if result == 'NO':
        for i in range(N):
            for j in range(N-5+1):
                cnt = 0
                for k in range(5):
                    if lst_N[j+k][i] == 'o':
                        cnt += 1
                    if cnt == 5:
                        result = 'YES'
                        break

    # 대각 1
    if result == 'NO':
        for i in range(N-5+1):
            for k in range(N-5+1):
                cnt = 0
                for j in range(5):
                    if lst_N[i+j][k+j] == 'o':
                        cnt += 1
                    if cnt == 5:
                        result = 'YES'
                        break

    if result == 'NO':
        for i in range(N-5+1):
            for k in range(N-1, 3, -1):
                cnt = 0
                for j in range(5):
                    if lst_N[i+j][k-j] == 'o':
                        cnt += 1
                    if cnt == 5:
                        result = 'YES'
                        break

    print(f'#{tc} {result}')