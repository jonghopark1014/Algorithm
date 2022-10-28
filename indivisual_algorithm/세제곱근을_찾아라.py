T = int(input())

for tc in range(1, T+1):
    N = int(input())
    start = 1
    end = 1000000
    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if mid ** 3 == N:
            ans = mid
            break
        elif mid ** 3 > N:
            end = mid - 1
        elif mid ** 3 < N:
            start = mid + 1
    print(f'#{tc} {ans}')