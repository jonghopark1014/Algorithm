# 테스트 케이스
T = int(input())

# N
for tc in range(1, T + 1):  
    N = int(input())
    a = list(map(int, input().split()))
    re_a = a[-1]
    profit = 0
    for i in range(len(a)-2, -1, -1):  
        if re_a < a[i]:  
            re_a = a[i]
        else:  
            profit += re_a - a[i]
    
    print(f'#{tc} {profit}')
            

