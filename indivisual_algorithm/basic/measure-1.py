T = int(input())

for tc in range(1, T+1):  
    N = int(input())
    print(f'#{tc}', end = ' ')
    measure = []
    for i in range(1, N+1):  
        if N % i == 0:  
            measure.append(i)
    measure.sort(reverse = True)
    for j in measure:  
        print(j, end = ' ')
    print()