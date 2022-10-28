import sys

N = int(sys.stdin.readline())

lst_N = list(map(int, sys.stdin.readline().split()))

idx_lst = []
stack = []
result = [0] * N
top = -1

for i in range(N):
    if top == -1:
        stack.append(lst_N[i])
        idx_lst.append(i)
        top += 1
    else:
        while top != -1:
            if lst_N[i] > stack[top]:
                stack.pop()
                top -= 1
                a = idx_lst.pop()
                result[a] = lst_N[i]
            else:
                stack.append(lst_N[i])
                idx_lst.append(i)
                top += 1
                break
        else:
            top += 1
            stack.append(lst_N[i])
            idx_lst.append(i)

for i in idx_lst:
    result[i] = -1

print(*result)