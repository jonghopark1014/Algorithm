def enqueue(item):
    global rear, Q
    rear += 1
    Q[rear] = item

def dequeue():
    global front, Q
    front += 1
    return Q[front]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst_N = list(map(int, input().split()))
    Q = [0] * 1000000
    rear = front = -1
    idx_lst = []
    while True:
        for idx in range(N):
            enqueue((idx, lst_N[idx]))
        while len(idx_lst) != M:
            a = dequeue()
            if a[1] // 2 == 0:
                idx_lst += [a[0]]
                idx += 1
                if idx > M-1:
                    enqueue((100, 100))
                else:
                    enqueue((idx, lst_N[idx]))
            else:
                enqueue((a[0], a[1] // 2))
        if len(idx_lst) == M:
            break

    print(f'#{tc} {idx_lst[-1]+1}')