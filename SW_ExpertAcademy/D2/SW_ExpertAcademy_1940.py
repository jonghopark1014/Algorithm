T = int(input())

for tc in range(1, T+1):  
    # N : 0 현재 속도 유지, 1 : 가속, 2: 감속
    sec = int(input())
    way = 0
    Speed = 0
    for i in range(sec):  
        ls_NS = list(map(int, input().split()))

        if len(ls_NS) == 2:  
            N = ls_NS[0]
            S = ls_NS[1]
        else:  
            N = ls_NS[0]
            
        if N == 0:  
            way += Speed
        elif N == 1:  
            Speed = Speed + S
            way += Speed
        else:  
            if Speed - S > 0:  
                Speed = Speed - S
                way += Speed
            elif Speed - S <= 0:  
                Speed = 0
    print(f'#{tc} {way}')