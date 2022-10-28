T = int(input())

for tc in range(1, T + 1):  
    N = int(input())
    b = [0, 0]
    N_l = [0] * N * N
    for i in range(1, N * N):  
        if i <= N:  
            N_l[b[0] * N + b[1]] = i
            b[1] += 1
        else:  
            if b[1] == N:  
                N_l[b[0] * N + b[1]-1] = i
                b[0] += 1
                if b[0] == N:  
                    N_l[b[0] * N - 1 + b[1]-1] = i
                    b[1] -= 1
                    if b[1] == 0:  
                        N_l[b[0] * N - 1 + b[1]-1] = i
                        b[0] -= 1
                        if b[0] == 1:  
                            N_l[b[0] * N - 1 + b[1]-1] = i
                            b[1] += 1
    
    print(N_l)



    




