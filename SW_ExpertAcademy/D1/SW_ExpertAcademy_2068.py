# 테스트 케이스
T = int(input())

# 수 입력받음
for tc in range(1, T+ 1):  
    a = list(map(int, input().split()))
    b = sorted(a)[9]
    print(f'#{tc} {b}')
