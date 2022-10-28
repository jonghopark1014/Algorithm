T = int(input())

for tc in range(1, T+1):  
    a, b, c = input().split()
    list_al = list(map(int, (a, b)))
    if c == '+':  
        d = list_al[0] + list_al[1]
        print(f'#{tc} {d}')
    elif c == '-':  
        d = list_al[0] - list_al[1]
        print(f'#{tc} {d}')
    elif c == '*': 
        d = list_al[0] * list_al[1]
        print(f'#{tc} {d}')
    else :  
        d = list_al[0] // list_al[1]
        print(f'#{tc} {d}')