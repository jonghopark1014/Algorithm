import sys

def push(x):
    global rear
    rear += 1
    Q[rear] = x

def popp():
    global start
    a = Q[start]
    start += 1
    if start > rear:
        start = rear + 1
    if a == 0:
        return -1
    else:
        return a

def size():
    global rear, start
    if rear - start + 1 > 0:
        return rear - start + 1
    else:
        return 0

def isEmpty():
    if rear >= start:
        return 0
    else:
        return 1

def front():
    if start <= rear:
        return Q[start]
    else:
        return -1

def back():
    if start <= rear:
        return Q[rear]
    else:
        return -1

N = int(sys.stdin.readline())
Q = [0] * 20000
rear, start = -1, 0
for i in range(N):
    tmp_lst = list(sys.stdin.readline().split())
    if len(tmp_lst) == 2:
        if tmp_lst[0] == 'push':
            push(tmp_lst[1])
    else:
        if tmp_lst[0] == 'front':
            print(front())
        elif tmp_lst[0] == 'back':
            print(back())
        elif tmp_lst[0] == 'size':
            print(size())
        elif tmp_lst[0] == 'empty':
            print(isEmpty())
        elif tmp_lst[0] == 'pop':
            print(popp())