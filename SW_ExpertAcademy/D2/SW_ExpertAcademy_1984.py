T = int(input())

for tc in range(1, T+1):  
    N = sorted(list(map(int, input().split())))
    re_N = N[1:len(N)-1]
    print(f'#{tc} {int(round(sum(re_N) / len(re_N), 0))}')