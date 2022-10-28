import sys
sys.stdin = open('sample_input (9).txt')

from collections import deque

T = int(input())

dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

ans_lst = []

for tc in range(1, T+1):
    N = int(input())
    lst_N = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    Q = deque()
    for r in range(0, N-2):
        for c in range(1, N-1):
            st_r, st_c = r, c
            if lst_N[r][c] == lst_N[r+1][c-1] or lst_N[r][c] == lst_N[r+1][c+1]:
                continue
            if ans >= (N - r - 1) * 2 + 1:
                break
            else:
                r2, c2 = r + dr[0], c + dc[0]
                tmp_sum = lst_N[r][c] + lst_N[r2][c2]
                check_lst = ''
                check_lst += str(lst_N[r][c]) + ' '
                check_lst += str(lst_N[r2][c2]) + ' '
                cnt = 2
                Q.append([r2, c2, 0, check_lst, cnt])
                while Q:
                    r3, c3, dir, check_lst2, cnt = Q.popleft()
                    for i in range(2):
                        dir += i
                        if dir < 4:
                            r4 = r3 + dr[dir]
                            c4 = c3 + dc[dir]
                            if st_r == r4 and st_c == c4:
                                if ans < cnt:
                                    ans = cnt
                            elif 0 <= r4 < N and 0 <= c4 < N:
                                check_lst3 = check_lst2 + str(lst_N[r4][c4]) + ' '
                                cnt += 1
                                tmp_lst = list(check_lst3.split())
                                if cnt == len(set(tmp_lst)):
                                    Q.append([r4, c4, dir, check_lst3, cnt])
                                    cnt -= 1
                                else:
                                    cnt -= 1
    ans_lst.append(f'#{tc} {ans}')
print('\n'.join(ans_lst))