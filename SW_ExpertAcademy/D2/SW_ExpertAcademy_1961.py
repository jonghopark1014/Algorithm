T = int(input())

for tc in range(1, T+1):  
    N = int(input())  
    ls_N = [list(input().split()) for i in range(N)]

    # 90도
    result1 = []
    for j in range(N):  
        a = []
        for k in range(N-1, -1, -1):  
            a.append(ls_N[k][j])
        re_n = ''.join(a)
        result1.append(re_n)

    # 180도
    result2 = []
    for l in range(N-1, -1, -1):  
        ls_p = [ ls_N[l][p] for p in range(N-1, -1, -1)  ]
        result2.append(''.join(ls_p))
    
    # 270도
    result3 = []
    for m in range(N-1, -1, -1):  
        b = []
        for o in range(N):  
            b.append(ls_N[o][m])
        result3.append(''.join(b))
    
    results = result1 + result2 + result3
    
    # 테스트 케이스 출력
    print(f'#{tc}')
    
    # 사각형으로 출력
    for num in range(N):
        for idx in range(num, len(results),N):  
            print(results[idx], end = ' ')
        print()
