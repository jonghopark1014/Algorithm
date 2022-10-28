T = int(input())

for tc in range(1, T+1):  
    H, W = map(int, input().split())
    a = 0
    b = 0
    print(f'#{tc}')
    for i in range(H):  
        b += 1
        for j in range(W):  
            if j == 0:  
                print(b, end= ' ')
                a = b
            else:  
                a += (W - 1)
                print(a, end = ' ')
        print()