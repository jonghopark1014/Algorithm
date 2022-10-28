T = int(input())

for tc in range(1, T+1):  
    N = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    re_N = N
    while re_N % 2 == 0:  
        a += 1
        re_N = re_N / 2

    while re_N % 3 == 0:  
        b += 1
        re_N = re_N / 3
    
    while re_N % 5 == 0:  
        c += 1
        re_N = re_N / 5
    
    while re_N % 7 == 0:  
        d += 1
        re_N = re_N / 7
    
    while re_N % 11 == 0:  
        e += 1
        re_N = re_N / 11
    
    print(f'#{tc} {a} {b} {c} {d} {e}')