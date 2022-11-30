import sys
from collections import deque


def push(x):
    Q.append(x)


def popp():
    if Q:
        a = Q.popleft()
        return a
    else:
        return -1


def size():
    return len(Q)


def isEmpty():
    if Q:
        return 0
    else:
        return 1


def front():
    if Q:
        return Q[0]
    else:
        return -1

def back():
    if Q:
        return Q[-1]
    else:
        return -1


N = int(sys.stdin.readline())
Q = deque()
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