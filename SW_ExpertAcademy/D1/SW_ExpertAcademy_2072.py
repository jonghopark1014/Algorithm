T = int(input()) # 테스트 케이스

for i in range(1, T+1):  # 테스트 케이스 만큼 반복 및 입력 받을 수
    N = map(int, input().split())
    sum = 0
    for j in N:   # 홀수 분류 및 덧셈
        if j % 2 != 0:  
            sum = sum + j
    print(f'#{i} {sum}')