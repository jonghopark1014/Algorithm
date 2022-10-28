T = int(input())

for tc in range(1, T+1):  
    N = int(input())
    lst_N = list(map(int, input().split()))
    for i in range(len(lst_N) -1, 0, -1):  
        for j in range(i):  
            if lst_N[j] > lst_N[j+1]:  
                lst_N[j], lst_N[j+1] = lst_N[j+1], lst_N[j]
    
    print(f'#{tc}', end = ' ')
    for k in lst_N:  
        print(k, end = ' ')
    print()