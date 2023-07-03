import sys

# input
input_read = sys.stdin.readline
H, W = map(int, input_read().split())
arr = list(map(int, input_read().split()))
ans = 0

L, R, LMax, RMax = 0, W - 1, arr[0], arr[W - 1]

# 투포인터 활용
while L < R:
    if LMax > RMax:
       ans += RMax - arr[R]
       R -= 1
       RMax = max(RMax, arr[R])
    else:
        ans += LMax - arr[L]
        L += 1
        LMax = max(LMax, arr[L])

print(ans)