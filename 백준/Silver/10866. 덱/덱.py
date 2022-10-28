from collections import deque
import sys

Q = deque()

def push_front(x):
    Q.appendleft(x)

def push_back(x):
    Q.append(x)

def isEmpty():
    if len(Q) == 0:
        print(1)

    else:
        print(0)

def pop_front():
    if len(Q) == 0:
        print(-1)

    else:
        a = Q.popleft()
        print(a)


def pop_back():
    if len(Q) == 0:
        print(-1)

    else:
        a = Q.pop()
        print(a)


def size():
    print(len(Q))

def front():
    if len(Q) == 0:
        print(-1)
    else:
        print(Q[0])


def back():
    if len(Q) == 0:
        print(-1)

    else:
        print(Q[-1])


for i in range(1, int(sys.stdin.readline()) + 1):
    a = list(map(str, sys.stdin.readline().split()))
    if len(a) == 2:
        if a[0] == 'push_back':
            push_back(a[1])
        elif a[0] == 'push_front':
            push_front(a[1])
    else:
        if a[0] == 'front':
            front()
        elif a[0] == 'back':
            back()
        elif a[0] == 'size':
            size()
        elif a[0] == 'empty':
            isEmpty()
        elif a[0] == 'pop_front':
            pop_front()
        elif a[0] == 'pop_back':
            pop_back()
