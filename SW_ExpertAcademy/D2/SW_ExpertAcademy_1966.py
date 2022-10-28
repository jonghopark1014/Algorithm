T = int(input())

for tc in range(1, T+1): 
    N = int(input())
    if 5 <= N <= 50:  
        num = list(map(int, input().split()))
        num.sort()
        print(f'#{tc}', end = ' ') 
        for i in range(N):  
            print(num[i], end = ' ')
        print()