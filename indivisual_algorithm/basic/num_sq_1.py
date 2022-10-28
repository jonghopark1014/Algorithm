T = int(input())

for tc in range(1, T+1):  
    H, W = map(int, input().split())
    a = 0
    print(f'#{tc}')
    for i in range(H):  
        for j in range(W):  
            a += 1
            print(a, end = ' ')
        print()