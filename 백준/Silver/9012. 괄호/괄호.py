import sys

N = int(sys.stdin.readline())

lst_n = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

def push(x):
    global top
    top += 1
    stack[top] = x

def popp():
    global top
    a = stack[top]
    stack[top] = 0
    top -= 1
    return a

for i in lst_n:
    stack = [0] * 51
    top = -1
    cnt = len(i)
    for j in i:
        if j == '(':
            push(j)
        elif j == ')':
            if stack[top] == '(':
                popp()
            else:
                push(j)
    if top != -1:
        print('NO')
    else:
        print('YES')
