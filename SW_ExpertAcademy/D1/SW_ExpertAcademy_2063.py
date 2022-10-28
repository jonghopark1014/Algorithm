# 입력값 개수
N = int(input())

# 입력값 나누기 및 정렬
score = list(map(int, input().split()))
score.sort()

# 입력값 중 중앙값 찾기
for i in range(N):  
    if i == N//2:  
        print(score[i])