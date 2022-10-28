import sys

tmp_lst_2 = []
while True:
    N = list(sys.stdin.readline().rstrip())
    if N == ['.']:
        break
    else:
        tmp_lst_2.append(N)


for i in tmp_lst_2:
    stack = []
    for j in i:
        if j == '(' or j == '[':
            stack.append(j)
        elif j == ']':
            if len(stack) == 0:
                print('no')
                break
            elif stack[-1] != '[':
                print('no')
                break
            else:
                stack.pop()
        elif j == ')':
            if len(stack) == 0:
                print('no')
                break
            elif stack[-1] != '(':
                print('no')
                break
            else:
                stack.pop()
    else:
        if len(stack) != 0:
            print('no')
        else:  
            print('yes')