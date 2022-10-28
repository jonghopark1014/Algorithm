# 정수 N
N = int(input())

# 약수 도출
for i in range(1, N+1):  
    if N % i == 0:  
        print(i, end=' ')