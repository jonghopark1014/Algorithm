import sys

Q = [0] * 10000000

start = -1
rear = -1
def push(x):
    global rear
    rear += 1
    Q[rear] = x

def popp():
    global start
    start += 1
    return Q[start]

lst_N = [i for i in range(1, int(sys.stdin.readline()) + 1)]

for i in lst_N:
    push(i)
while start <= rear:
    a = popp()
    b = popp()
    if b != 0:
        push(b)
    else:
        break

print(a)
