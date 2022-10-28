T = int(input())

for tc in range(1, T+1):  
    N, M = map(int, input().split())
    print(f'#{tc}')
    if M == 1:  
        for a in range(N):  
            for b in range(a+1):  
                print('*', end = '')
            print()
    elif M == 2:  
        for a in range(N, 0, -1):  
            for b in range(a):  
                print('*', end = '')
            print()
    else :  
        for a in range(N):  
            for b in range(N-a-1):  
                print(' ', end = '')
            for c in range(2 * a + 1):  
                print('*', end = '')
            print()
