T = int(input())

for tc in range(1, T+1):  
    N = int(input())
    print(f'#{tc}')
    for i in range(N):  
        for k in range(N-i-1):  
            print(' ', end = '')
        for j in range(i+1):  
            print('*', end = '')
        print()