from collections import deque

T = int(input())

dr = [0, 1]
dc = [1, 0]

def minSum(r, c, cnt):
    global ans
    Q = deque()
    Q.append([r, c, cnt])
    while Q:
        r, c, cnt = Q.popleft()
        for i in range(2):
            r2 = r + dr[i]
            c2 = c + dc[i]
            if 0 <= r2 < N and 0 <= c2 < N:
                cnt += lst_N[r2][c2]
                if not used[r2][c2]:
                    Q.append([r2, c2, cnt])
                    used[r2][c2] = cnt
                else:
                    if cnt < used[r2][c2]:
                        Q.append([r2, c2, cnt])
                        used[r2][c2] = cnt
                cnt -= lst_N[r2][c2]

tmp_lst = []
for tc in range(1, T+1):
    ans = 999999
    N = int(input())
    lst_N = [list(map(int, input().split())) for _ in range(N)]
    used = [[0] * N for _ in range(N)]
    minSum(0, 0, lst_N[0][0])
    tmp_lst.append(f'#{tc} {used[N-1][N-1]}')

print('\n'.join(tmp_lst))