from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input()) + 1):
    N = int(input())
    lst_N = [list(map(int, input().split())) for _ in range(N)]
    value_lst = [[5000000] * N for _ in range(N)]
    Q = deque()
    Q.append([0, 0, 0])
    value_lst[0][0] = 0

    while Q:
        r, c, cnt = Q.popleft()
        if value_lst[r][c] < cnt:
            continue
        for i in range(4):
            r2 = r + dr[i]
            c2 = c + dc[i]
            if 0 <= r2 < N and 0 <= c2 < N:
                a = lst_N[r2][c2] - lst_N[r][c]
                if a > 0:
                    tmp = 1 + a + cnt
                else:
                    tmp = cnt + 1
                if value_lst[r2][c2] > tmp:
                    value_lst[r2][c2] = tmp
                    Q.append([r2, c2, tmp])


    print(f'#{tc}', value_lst[N-1][N-1])

'''
힙큐
import heapq

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

for tc in range(1, int(input()) + 1):
    N = int(input())
    lst_N = [list(map(int, input().split())) for _ in range(N)]
    visited = [[9999999] * N for _ in range(N)]
    visited[0][0] = 0
    heap = []
    heapq.heappush(heap, (0, 0, 0))

    while len(heap) > 0:
        cnt, r, c = heapq.heappop(heap)
        for i in range(4):
            r2 = r + dr[i]
            c2 = c + dc[i]
            if 0 <= r2 < N and 0 <= c2 < N:
                tmp = cnt + 1
                if lst_N[r2][c2] > lst_N[r][c]:
                    tmp += lst_N[r2][c2] - lst_N[r][c]
                if visited[r2][c2] > tmp:
                    visited[r2][c2] = tmp
                    heapq.heappush(heap, (tmp, r2, c2))
    print(f'#{tc}', visited[N-1][N-1])
'''