T = int(input())

for tc in range(1, T+1):  
    a, b = map(int, input().split())
    c = []
    print(f'#{tc}', end = ' ')
    for i in range(1, int((b/a) + 1)):  
        print(a * i, end = ' ')
    print()