N = int(input())

if N == 0:  
    print(1)
else:  
    count = 0
    re_N = N
    A = 0
    while N != A:  
        count += 1
        if re_N < 10:  
            re_N = re_N*10 + re_N
        else:  
            if re_N // 10 + re_N % 10 >= 10:  
                re_N = (re_N%10*10) + (re_N // 10 + re_N % 10)%10
            else:  
                re_N = (re_N%10*10) + (re_N // 10 + re_N % 10)
        A = re_N

    print(count)