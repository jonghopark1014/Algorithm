T = int(input())

for tc in range(1, T+1):  
    N = int(input())
    lst_N = list(map(int, input().split()))
    sum_max = 0
    for i in range(N-1):  
        if lst_N[i] + lst_N[i+1] > sum_max:  
            sum_max = lst_N[i] + lst_N[i+1]
    
    print(f'#{tc} {sum_max}')