T = int(input())

def enqueue(item):
    global rear
    rear += 1
    Q[rear] = item

def dequeue():
    global front
    front += 1
    return Q[front]

for tc in range(1, T+1):
    N = int(input())
    Q = [0] * 1000000
    rear = front = -1
    for i in range(1, N+1):
        enqueue(i)
    while rear != front:
        a = dequeue()
        if front % 2:
            enqueue(a)

    print(f'#{tc}', Q[front])
