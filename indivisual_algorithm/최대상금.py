T = int(input())

def dfs(cnt):
    global result
    a = int(''.join(arr_num))
    if a in used[cnt]:
        return
    else:
        used[cnt].add(a)
    if cnt == C:
        if int(''.join(arr_num)) > result:
            result = int(''.join(arr_num))
        return
    for i in range(N - 1):
        for j in range(i+1, N):
            arr_num[i], arr_num[j] = arr_num[j], arr_num[i]
            dfs(cnt + 1)
            arr_num[i], arr_num[j] = arr_num[j], arr_num[i]


for tc in range(1, T+1):
    numb, C = input().split()
    C = int(C)
    arr_num = list(numb)
    N = len(arr_num)
    used = [set() for _ in range(C + 1)]
    result = 0
    dfs(0)
    print(f'#{tc}', result)

# from collections import deque
# T = int(input())
#
# def bfs(value):
#     global result, cnt
#     Q = deque()
#     Q.append([value, cnt])
#
#     while Q:
#         value2, cnt2 = Q.popleft()
#         value2 = list(value2)
#         if cnt2 == C:
#             if int(''.join(value2)) > result:
#                 result = int(''.join(value2))
#         else:
#             cnt2 += 1
#             for i in range(N - 1):
#                 for j in range(i+1, N):
#                     value2[i], value2[j] = value2[j], value2[i]
#                     a = ''.join(value2)
#                     if a not in used[cnt2]:
#                         used[cnt2].add(a)
#                         Q.append([a, cnt2])
#                     value2[i], value2[j] = value2[j], value2[i]
#
# for tc in range(1, T+1):
#     numb, C = input().split()
#     cnt = 0
#     C = int(C)
#     N = len(numb)
#     result = 0
#     used = [set() for _ in range(C + 1)]
#     bfs(numb)
#     print(f'#{tc}', result)