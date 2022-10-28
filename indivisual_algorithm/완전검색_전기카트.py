# from collections import deque
#
# T = int(input())
#
# def minEnergy(r, c, ener, used):
#     global ans
#     Q = deque()
#     used = list(used)
#     used[r], used[c] = '1', '1'
#     ener += lst_N[r][c]
#     Q.append([r, c, ener, ''.join(used)])
#
#     while Q:
#         r, c, ener, used = Q.popleft()
#         r2 = c
#         used = list(used)
#         for i in range(N):
#             if used[i] != '1':
#                 ener += lst_N[r2][i]
#                 if ans > ener:
#                     used[i] = '1'
#                     Q.append([r2, i, ener, ''.join(used)])
#                     ener -= lst_N[r2][i]
#                     used[i] = '0'
#         if used == ['1'] * N:
#             ener += lst_N[r2][0]
#             if ans > ener:
#                 ans = ener
#
# for tc in range(1, T+1):
#     ans = 999999
#     N = int(input())
#     lst_N = [list(map(int, input().split())) for _ in range(N)]
#     used = '0' * N
#     for i in range(1, N):
#         minEnergy(0, i, 0, used)
#     print(f'#{tc}', ans)

# T = int(input())
#
# def minEnergy(x, energy):
#     global ans
#     if energy > ans:
#         return
#     if visited == [1] * N:
#         energy += lst_N[x][0]
#         if energy < ans:
#             ans = energy
#     visited[x] = True
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             energy += lst_N[x][i]
#             minEnergy(i, energy)
#             visited[i] = False
#             energy -= lst_N[x][i]
#
# for tc in range(1, T+1):
#     ans = 999999
#     N = int(input())
#     lst_N = [list(map(int, input().split())) for _ in range(N)]
#     for i in range(1, N):
#         visited = [False] * N
#         visited[0] = True
#         minEnergy(i, lst_N[0][i])
#     print(f'#{tc}', ans)

T = int(input())

def minEnergy(x, energy, level):
    global ans
    if level == N:
        energy += lst_N[x][0]
        if energy < ans:
            ans = energy
            return
    elif energy >= ans:
        return

    for i in range(N):
        if not visited[i] and i != x:
            visited[i] = True
            minEnergy(i, energy + lst_N[x][i], level + 1)
            visited[i] = False

for tc in range(1, T+1):
    ans = 999999
    N = int(input())
    lst_N = [list(map(int, input().split())) for _ in range(N)]
    for i in range(1, N):
        visited = [False] * N
        visited[0] = True
        visited[i] = True
        minEnergy(i, lst_N[0][i], 2)
    print(f'#{tc}', ans)
