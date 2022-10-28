import sys

N = int(sys.stdin.readline())

lst_N = [i for i in range(1, N + 1)]

stack = []

ans_lst = []

n_top = 0
for i in range(N):
    tmp_num = int(input())
    while n_top < N:
        if stack:
            while n_top < N:
                if stack[-1] != tmp_num:
                    stack.append(lst_N[n_top])
                    n_top += 1
                    ans_lst.append('+')
                else:
                    target = stack.pop()
                    ans_lst.append('-')
                    break
            if ans_lst[-1] == '-':
                break
        else:
            stack.append(lst_N[n_top])
            n_top += 1
            ans_lst.append('+')
    else:
        if stack[-1] == tmp_num:
            stack.pop()
            ans_lst.append('-')
        else:
            break

if stack:
    print('NO')
else:
    print('\n'.join(ans_lst))
