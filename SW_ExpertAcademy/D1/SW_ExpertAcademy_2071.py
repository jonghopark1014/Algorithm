# 테스트 케이스 
T = int(input())

for tc in range(1, T + 1):  
    a = list(map(int, input().split()))
    average = sum(a) / len(a) # 평균내기
    print(f'#{tc} {round(average)}') # tc와 반올림 값 출력
