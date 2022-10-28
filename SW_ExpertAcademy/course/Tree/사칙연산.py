# def incoder(x):
#     global stack
#     if x == 0: return
#     incoder(L[x])
#     incoder(R[x])
#     if str(tree[x]).isdigit():
#         stack.append(tree[x])
#     if tree[x] == '-':
#             a = stack.pop()
#             b = stack.pop()
#             tree[x] = b - a
#             stack.append(tree[x])
#     elif tree[x] == '*':
#         a = stack.pop()
#         b = stack.pop()
#         tree[x] = b * a
#         stack.append(tree[x])
#     elif tree[x] == '+':
#         a = stack.pop()
#         b = stack.pop()
#         tree[x] = b + a
#         stack.append(tree[x])
#     elif tree[x] == '/':
#         a = stack.pop()
#         b = stack.pop()
#         tree[x] = b / a
#         stack.append(tree[x])
#
# for tc in range(1, 11):
#     N = int(input())
#     L = [0] * (N + 1)
#     R = [0] * (N + 1)
#     tree = [0] * (N + 1)
#     stack = []
#     for i in range(N):
#         tmp_lst = list(input().split())
#         if len(tmp_lst) == 4:
#             tree[int(tmp_lst[0])] = tmp_lst[1]
#             L[int(tmp_lst[0])] = int(tmp_lst[2])
#             R[int(tmp_lst[0])] = int(tmp_lst[3])
#         else:
#             tree[int(tmp_lst[0])] = int(tmp_lst[1])
#     incoder(1)
#     print(f'#{tc} {int(tree[1])}')
#
# ================================
import sys

sys.stdin = open('input.txt')

# def incoder(x):
#     global C
#     if x == 0:
#         return
#     incoder(L[x])
#     incoder(R[x])
#     if tree[x] == '-':
#         tree[x] = tree[C[x][0]] - tree[C[x][1]]
#     elif tree[x] == '*':
#         tree[x] = tree[C[x][0]] * tree[C[x][1]]
#     elif tree[x] == '+':
#         tree[x] = tree[C[x][0]] + tree[C[x][1]]
#     elif tree[x] == '/':
#         tree[x] = tree[C[x][0]] / tree[C[x][1]]
#
# for tc in range(1, 11):
#     N = int(input())
#     L = [0] * (N + 1)
#     R = [0] * (N + 1)
#     C = [[] for _ in range(N+1)]
#     tree = [0] * (N + 1)
#
#     for _ in range(N):
#         tmp_lst = list(input().split())
#         if len(tmp_lst) == 4:
#             L[int(tmp_lst[0])] = int(tmp_lst[2])
#             R[int(tmp_lst[0])] = int(tmp_lst[3])
#             C[int(tmp_lst[0])].append(int(tmp_lst[2]))
#             C[int(tmp_lst[0])].append(int(tmp_lst[3]))
#         if str(tmp_lst[1]).isdigit():
#             tree[int(tmp_lst[0])] = int(tmp_lst[1])
#         else:
#             tree[int(tmp_lst[0])] = tmp_lst[1]
#     incoder(1)
#
#     print(f'#{tc} {int(tree[1])}')


# =================================

def incoder(x):
    if len(tree[x]) == 2:
        return int(tree[x][1])
    else:
        left = incoder(int(tree[x][2]))
        right = incoder(int(tree[x][3]))
        operator = tree[x][1]
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return left / right

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    for i in range(N):
        tmp_lst = input().split()
        tree[int(tmp_lst[0])] = tmp_lst
    print(f'#{tc} {int(incoder(1))}')
