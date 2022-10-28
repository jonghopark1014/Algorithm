for tc in range(1, 11):  
    N = int(input())

    lst_N = list(map(int, input().split()))

    count = 0
    for i in range(2,N-5+3):  
        if lst_N[i] > lst_N[i-2] and lst_N[i] > lst_N[i+2] and lst_N[i] > lst_N[i+1] and lst_N[i] > lst_N[i-1]:  
            if lst_N[i-2] >= lst_N[i-1] and lst_N[i-2] >= lst_N[i+1] and lst_N[i-2] >= lst_N[i+2]:  
                count += lst_N[i] - lst_N[i-2]
            elif lst_N[i-1] >= lst_N[i-2] and lst_N[i-1] >= lst_N[i+1] and lst_N[i-1] >= lst_N[i+2]:  
                count += lst_N[i] - lst_N[i-1]
            elif lst_N[i+1] >= lst_N[i-2] and lst_N[i+1] >= lst_N[i-1] and lst_N[i+1] >= lst_N[i+2]:  
                count += lst_N[i] - lst_N[i+1]
            elif lst_N[i+2] >= lst_N[i-2] and lst_N[i+2] >= lst_N[i-1] and lst_N[i+2] >= lst_N[i+1]:  
                count += lst_N[i] - lst_N[i+2]
    print(f'#{tc} {count}')