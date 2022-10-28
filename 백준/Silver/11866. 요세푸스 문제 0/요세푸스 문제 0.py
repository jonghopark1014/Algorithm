from collections import deque

N, K = map(int, input().split())

Q = deque()

for i in range(1, N+1):
    Q.append(i)

cnt = 0
if N == 1:
    print(f'<{Q.popleft()}>')
while Q:
    cnt += 1
    if cnt % K == 0:
        if cnt == K:
            a = Q.popleft()
            print(f'<{a},', end=' ')
        elif len(Q) == 1:
            a = Q.popleft()
            print(f'{a}>')
        else:
            a = Q.popleft()
            print(f'{a},', end = ' ')
    else:
        a = Q.popleft()
        Q.append(a)
