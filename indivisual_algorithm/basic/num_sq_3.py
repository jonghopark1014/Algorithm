T = int(input())

for tc in range(1, T+1):  
    H, W = map(int, input().split())
    print(f'#{tc}')
    a = 1
    b = 2
    for i in range(1, H+1):  
        if i % 2 == 0:  
            for k in range(W*b, W * (b-1), -1):  
                print(k, end = ' ')
            b += 2
        else:  
            for j in range(a, W+a):  
                print(j, end = ' ')
            a += 2*W
        print()