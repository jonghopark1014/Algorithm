# 테스트 케이스
T = int(input())

# divmod 사용해 몫, 나머지 출력
for tc in range(1, T+1):  
    a, b = map(int, input().split())
    a, b = divmod(a, b)
    print(f'#{tc} {a} {b}')