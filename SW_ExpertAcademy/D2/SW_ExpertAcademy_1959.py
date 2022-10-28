T = int(input())

for tc in range(1, T+1):  
    N, M = map(int, input().split())
    arr_N = list(map(int, input().split()))
    arr_M = list(map(int, input().split()))

    print(f'#{tc}', end = ' ')
    # 3가지 케이스로 나누기
    if N < M:  
        sum_ls = []
        for i in range(M-N+1):  
            sum_MN = []
            re_M = arr_M[i : i + N]
            for i in range(N):  
                sum_MN.append(arr_N[i] * re_M[i])
            sum_ls.append(sum(sum_MN))
        print(max(sum_ls))
    elif N == M:  
        sum_MN = [arr_N[i] * arr_M[i] for i in range(N)]
        print(sum(sum_MN))
    else:  
        sum_ls = []
        for i in range(N-M+1):  
            sum_MN = []
            re_N = arr_N[i : i + M]
            for i in range(M):  
                sum_MN.append(arr_M[i] * re_N[i])
            print(sum_MN)
            sum_ls.append(sum(sum_MN))
        print(max(sum_ls))