def enqueue(item):
    global rear
    rear = rear+1
    Q[rear] = item

def dequeue():
    global front
    front = front+1
    return Q[front]

for tc in range(1, 11):
    T = int(input())
    lst_N = list(map(int, input().split()))
    Q = [0] * 1000000
    front = rear = -1
    for i in lst_N:
        enqueue(i)
    while True:
        for i in range(1, 6):
            a = dequeue()
            enqueue(a-i)
            if a-i <= 0:
                Q[rear] = 0
                break
        if a - i <= 0:
            break
    print(f'#{tc}', end = ' ')
    for i in range(rear-7, rear+1):
        print(Q[i], end = ' ')
    print()

