T = int(input())

for tc in range(1, T+1):  
    N = int(input())
    re_n = [1, 1]
    print(f'#{tc}')
    for c in range(0, N):  
        if c == 0:  
            al_n = [[1]]
        elif c == 1: 
            al_n = [[1], [1,1]]
        else:  
            al_n.append([1,1])
            for i in range(c-1):  
                al_n[c].insert(i+1, sum(re_n[i:i+2]))
        
            re_n = al_n[c]
    
    for j in al_n:  
        for k in range(len(j)):  
            print(j[k], end = ' ')
        print()