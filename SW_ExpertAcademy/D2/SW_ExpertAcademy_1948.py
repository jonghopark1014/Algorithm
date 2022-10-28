T = int(input())

for tc in range(1, T + 1):  
    N = list(map(int, input().split()))
    print(f'#{tc}', end = ' ')
    if N[0] == N[2]:  
        print(N[3] - N[1] + 1)
    else:  
        sum_m = 0
        for i in range(N[0], N[2]):  
            if i == 2:  
                sum_m += 28
            elif i in [4, 6, 9, 11]:  
                sum_m += 30
            else:  
                sum_m += 31
        print(sum_m + N[3] - N[1] + 1)
