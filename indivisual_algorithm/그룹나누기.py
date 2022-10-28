# from collections import deque
#
# def bfs(x):
#     Q = deque()
#     Q.append(x)
#
#     while Q:
#         x = Q.popleft()
#         for i in range(1, N + 1):
#             if G[x][i] == 1 and not visited[i]:
#                 visited[i] = True
#                 Q.append(i)
#
#
# for tc in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     couple = list(map(int, input().split()))
#     G = [[0] * (N + 1) for _ in range(N + 1)]
#     ans = 0
#     visited = [False] * (N + 1)
#     for i in range(0, M*2, 2):
#         G[couple[i]][couple[i+1]] = 1
#         G[couple[i+1]][couple[i]] = 1
#     for i in range(1, N + 1):
#         if not visited[i]:
#             visited[i] = True
#             bfs(i)
#             ans += 1
#
#     print(f'#{tc}', ans)

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    couple = list(map(int, input().split()))
    ans = N - M
    check_set = set()
    len_set = 0
    for i in range(0, M * 2, 2):
        check_set.add(couple[i])
        check_set.add(couple[i + 1])
        len_set += 2
        if len_set - len(check_set) > 1:
            ans += 1
            break
        else:
            len_set = len(check_set)
    print(f'#{tc}', ans)