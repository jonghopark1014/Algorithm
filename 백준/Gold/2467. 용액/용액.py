import sys


# input
read_input = sys.stdin.readline

N = int(read_input())
arr = list(map(int, read_input().split()))
mix = 2000000001
L, R = 0, N - 1
ans = [0, 0]

while L < R:
    tmp = arr[L] + arr[R]

    if not tmp or not tmp * -1:
        ans = [arr[L], arr[R]]
        break

    if tmp < 0 :
        if (tmp * -1) < mix:
            mix = tmp * -1
            ans = [arr[L], arr[R]]
        L += 1

    elif tmp > 0:
        if tmp < mix:
            mix = tmp
            ans = [arr[L], arr[R]]
        R -= 1

print(*ans)