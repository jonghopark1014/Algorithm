T = int(input())

for tc in range(1, T+1):  
    i_t, i_m, j_t, j_m = map(int, input().split())
    sum_t = i_t + j_t
    sum_m = i_m + j_m
    if sum_m > 60:  
        sum_t = sum_t + 1
        sum_m = sum_m - 60
        if sum_t > 12:  
            sum_t = sum_t - 12
        print(f'#{tc} {sum_t} {sum_m}')
    else:  
        if sum_t > 12:  
            sum_t = sum_t - 12
        print(f'#{tc} {sum_t} {sum_m}')
