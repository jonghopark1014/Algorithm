T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst_N = [list(input()) for _ in range(N)]

    # 가로
    result = 'NO'
    for i in range(len(lst_N)):
        for j in range(N):
            if lst_N[i][j] == 'o':
                cnt = 1
                while True:
                    j += 1
                    cnt += 1
                    if j >= N:
                        cnt -= 1
                        if cnt >= 5:
                            result = 'YES'
                            break
                        else:
                            break
                    elif lst_N[i][j] != 'o':
                        cnt -= 1
                        if cnt >= 5:
                            result = 'YES'
                            break
                        else:
                            break
            if result == 'YES':
                break
        if result == 'YES':
            break
    # 세로
    if result != 'YES':
        for j in range(N):
            for i in range(N):
                if lst_N[j][i] == 'o':
                    cnt = 1
                    while True:
                        j += 1
                        cnt += 1
                        if j >= N:
                            cnt -= 1
                            if cnt >= 5:
                                result = 'YES'
                                break
                            else:
                                j -= cnt
                                break
                        elif lst_N[j][i] != 'o':
                            cnt -= 1
                            if cnt >= 5:
                                result = 'YES'
                                break
                            else:
                                j -= cnt
                                break
                if result == 'YES':
                    break
            if result == 'YES':
                break
    # 대각선 1
    if result != 'YES':
        for i in range(N):
            for j in range(N):
                if lst_N[i][j] == 'o':
                    cnt = 1
                    while True:
                        i += 1
                        j += 1
                        cnt += 1
                        if j >= N or i >= N:
                            cnt -= 1
                            if cnt >= 5:
                                result = 'YES'
                                break
                            else:
                                i -= cnt
                                break
                        elif lst_N[i][j] != 'o':
                            cnt -= 1
                            if cnt >= 5:
                                result = 'YES'
                                break
                            else:
                                i -= cnt
                                break
                if result == 'YES':
                    break
            if result == 'YES':
                break
    # 대각선 2
    if result != 'YES':
        for i in range(N):
            for j in range(N-1, -1, -1):
                if lst_N[i][j] == 'o':
                    cnt = 1
                    while True:
                        i += 1
                        j -= 1
                        cnt += 1
                        if j < 0 or i >= N:
                            cnt -= 1
                            if cnt >= 5:
                                result = 'YES'
                                break
                            else:
                                i -= cnt
                                break
                        elif lst_N[i][j] != 'o':
                            cnt -= 1
                            if cnt >= 5:
                                result = 'YES'
                                break
                            else:
                                i -= cnt
                                break
                if result == 'YES':
                    break
            if result == 'YES':
                break
    print(f'#{tc} {result}')