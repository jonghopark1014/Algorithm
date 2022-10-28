T = int(input())

for tc in range(1, T+1):  
    N = input()
    fix_n = 0
    ap_n = []
    i = 0

    while True:  
        i += 1

        fix_n = str(int(N) * i)
        
        for j in list(fix_n):  
            ap_n.append(int(j))
        
        
        if set(ap_n) == {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}:  
            break

    print(f'{tc} {fix_n}')

    

    




