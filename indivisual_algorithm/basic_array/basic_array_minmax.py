T = int(input())

for tc in range(1, T+1):  
    N = int(input()) # 양수 개수 N
    lst_N = list(map(int, input().split()))
    # 최소값 최대값 인덱스 찾기
    min_N = []
    max_N = []
    min_num = lst_N[0]
    max_num = lst_N[0]
    # 최소값
    for i in range(1, len(lst_N)):  
        if min_num > lst_N[i]:  
            min_num = lst_N[i]
    # 최대 값
    for j in range(1, len(lst_N)):  
        if max_num < lst_N[j]:  
            max_num = lst_N[j]
    
    # 인덱스 찾기
    for k in range(len(lst_N)):  
        if min_num == lst_N[k]:  
            min_N.append(k)
        elif max_num == lst_N[k]:  
            max_N.append(k)

    minus_min_max = min_N[0] - max_N[-1]

    if minus_min_max < 0:  
        print(f'#{tc} {minus_min_max * -1}')
    else:  
        print(f'#{tc} {minus_min_max}')