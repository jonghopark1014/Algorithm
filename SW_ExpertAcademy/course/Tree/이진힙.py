T = int(input())

def push(value):
    global hsize
    hsize += 1
    H[hsize] = value

    c = hsize
    p = c // 2
    while p and H[p] > H[c]:
        H[p], H[c] = H[c], H[p]
        c = p
        p = c // 2

for tc in range(1, T+1):
    N = int(input())
    tmp_lst = list(map(int, input().split()))
    H = [0] * (N + 1)
    hsize = 0
    for i in tmp_lst:
        push(i)
    ans = 0
    a = N
    while True:
        a = a // 2
        if not a:
            break
        ans += H[a]
    print(f'#{tc}', ans)