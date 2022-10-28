T = int(input())

for tc in range(1, T+1):  
    N = int(input())
    lst_N = list(map(int, input().split()))
    print(f'#{tc}', end = ' ')
    # 최대 최소값 추출
    minV = lst_N[0]
    maxV = 0
    for i in range(N):  
        if lst_N[i] > maxV:  
            maxV = lst_N[i]
    for j in range(1, N):  
        if lst_N[j] < minV:  
            minV = lst_N[j]
    
    #최대 최소 중복 인덱스 추출
    minV_lst = []
    maxV_lst = []
    for k in range(N):  
        if minV == lst_N[k]:  
            minV_lst.append(k)
        elif maxV == lst_N[k]:  
            maxV_lst.append(k)


    if minV_lst[0] - maxV_lst[-1] < 0:  
        print((minV_lst[0] - maxV_lst[-1])*-1)
    else:  
        print(minV_lst[0] - maxV_lst[-1])
    print()