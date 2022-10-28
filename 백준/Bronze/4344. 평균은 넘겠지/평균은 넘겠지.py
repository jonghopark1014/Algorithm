import sys

T = int(sys.stdin.readline())

for tc in range(1, T+1):  
    N_lst = list(map(int, sys.stdin.readline().split()))
    mean_N = sum(N_lst[1:])/N_lst[0]
    count_N = 0
    for i in N_lst[1:]:  
        if i > mean_N:  
            count_N += 1
    
    print('%.3f'%(count_N/N_lst[0] * 100) + '%')