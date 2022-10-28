T = int(input())

for tc in range(1, T+1):  
    N, M = map(int, input().split())
    N_l = []
    for i in range(N):  
        num_l = list(map(int, input().split()))
        N_l.append(num_l)

    sum_l = []
    for j in range(N-M+1):  
        for k in range(N - M + 1):  
            sum_n = 0
            for l in range(M):  
                a = sum(N_l[j+l][k:k+M])
                sum_n += a
            sum_l.append(sum_n)
    
    sum_l.sort()
    print(sum_l)
    print(f'#{tc} {sum_l[-1]}')



