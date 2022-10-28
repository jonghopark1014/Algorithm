T = int(input())

for tc in range(1, T+1):  
    N, K = map(int, input().split())
    n_ls = []
    count = 0
    for i in range(N):  
        n_ls.append(list(input().split()))
    
    # 가로 조건
    for j in n_ls:  
        for l in range(K, N+1):  
            if ['1'] * K == j[l-K: l]: 
                if l == K:  
                    if j[l] != '1':
                        count += 1
                elif l == N:  
                    if j[l-K-1] != '1':  
                        count += 1
                else:  
                    if j[l-K-1] != '1' and j[l] != '1':  
                        count += 1
    # 세로 -> 가로 변경
    c_ls = list(map(list,zip(*n_ls)))
    # 가로 조건 적용
    for m in c_ls:  
        for n in range(K, N+1):  
            if ['1'] * K == m[n-K:n]:  
                if n == K:  
                    if m[n] != '1':
                        count += 1
                elif n == N:  
                    if m[n-K-1] != '1':  
                        count += 1
                else:  
                    if m[n] == '0' and m[n-K-1] == '0':  
                        count += 1
    print(f'#{tc}', end = ' ')
    print(count)