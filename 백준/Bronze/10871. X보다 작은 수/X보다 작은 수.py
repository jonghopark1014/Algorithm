N, X = map(int, input().split())
N_lst = list(map(int, input().split()))
for i in N_lst:  
    if i < X:  
        print(i, end=' ')