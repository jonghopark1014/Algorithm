# 테스트 케이스
T = int(input())

# 테스트 케이스 평가
for tc in range(1, T + 1):  
    a, b = map(int, input().split())

    if a > b :  
        print(f'#{tc} >')
    elif a == b :  
        print(f'#{tc} =')
    else:  
        print(f'#{tc} <')