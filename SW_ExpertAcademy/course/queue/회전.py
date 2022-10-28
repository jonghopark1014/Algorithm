def enqueue(x):
    global rear, Q
    rear += 1
    Q[rear] = x

def dequeue():
    global front, Q
    front += 1
    return Q[front]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int ,input().split())
    lst_N = list(map(int, input().split()))
    rear = -1
    front = -1
    Q = [0] * 20000
    for i in lst_N:
        enqueue(i)
    for j in range(M):
        a = dequeue()
        enqueue(a)

    print(f'#{tc} {Q[front+1]}')