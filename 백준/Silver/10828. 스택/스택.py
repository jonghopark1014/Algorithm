import sys

def Push(v):
    global top
    top += 1
    stack[top] = v

def Pop():
    global top
    value = stack[top]
    top -= 1
    if top < -1:
        top = -1
        return -1
    else:
        return value

def isEmpty():
    if top <= -1:
        return 1
    else:
        return 0

def Size():
    global top
    if top <= -1:
        return 0
    else:
        return top + 1

def Top():
    if top > -1:
        return stack[top]
    else:
        return -1

N = int(sys.stdin.readline())

stack = [0] * (N+1)
top = -1

for i in range(N):
    tmp_lst = list(sys.stdin.readline().split())
    if tmp_lst[0] == 'push':
        Push(tmp_lst[1])
    elif tmp_lst[0] == 'top':
        print(Top())
    elif tmp_lst[0] == 'size':
        print(Size())
    elif tmp_lst[0] == 'empty':
        print(isEmpty())
    elif tmp_lst[0] == 'pop':
        print(Pop())
