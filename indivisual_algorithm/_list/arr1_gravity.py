T = int(input())

for tc in range(1, T+1):  
    N = int(input())
    lst_N = list(map(int, input().split()))
    result = 0
    for i in range(len(lst_N)):  
        count = 0
        for j in range(i+1, len(lst_N)):  
            if lst_N[i] > lst_N[j]:  
                count += 1
        if count > result:  
            result = count
        
        if N-i < result:  
            break
    
    print(f'#{tc} {result}')