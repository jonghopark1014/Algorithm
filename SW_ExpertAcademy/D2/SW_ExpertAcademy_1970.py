T = int(input())

for tc in range(1, T+1):  
    N = int(input())
    t_ls = []
    if 10<= N <= 1000000:  
        money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
        print(f'#{tc}')
        for i in money:  
            t_ls.append(N // i)
            N = N - (i *(N//i))
        for j in t_ls:  
            print(j, end = ' ')
        print()
