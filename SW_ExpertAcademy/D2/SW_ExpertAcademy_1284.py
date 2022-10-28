T = int(input())

for tc in range(1, T+1):  
    P, Q, R, S, W = map(int, input().split())
    A_pay = P * W
    if W <= R:  
        B_pay = Q
    else:  
        B_pay = Q + ((W - R)*S)
    
    if A_pay < B_pay:  
        print(f'#{tc} {A_pay}')
    else:  
        print(f'#{tc} {B_pay}')