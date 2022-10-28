import sys
sys.stdin = open("input_mag.txt")

for tc in range(1, 11):
    N = int(input())
    lst_N = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        a = 0
        stack = []
        while True:
            if a == N:
                break
            if lst_N[a][i] == 1:
                stack.append(1)
            elif len(stack) > 0:
                if lst_N[a][i] == 2:
                    stack = []
                    cnt += 1
            a += 1

    print(f'#{tc} {cnt}')