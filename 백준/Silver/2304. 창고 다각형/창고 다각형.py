import sys

N = int(sys.stdin.readline())

lst_N = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

lst_N.sort(key = lambda x: x[0])

max_h = max(lst_N, key = lambda x : x[1])
result = max_h[1]

for i in range(len(lst_N)):
    if lst_N[i] == max_h:
        idx_max = i
        break

left1 = 0
left2 = 1
right1 = N - 1
right2 = N - 2

while left1 != idx_max:
    if lst_N[left1][1] <= lst_N[left2][1]:
        result += (lst_N[left2][0] - lst_N[left1][0]) * lst_N[left1][1]
        left1 = left2
        left2 += 1
    else:
        left2 += 1

while right1 != idx_max:
    if lst_N[right1][1] <= lst_N[right2][1]:
        result += (lst_N[right1][0] - lst_N[right2][0]) * lst_N[right1][1]
        right1 = right2
        right2 -= 1
    else:
        right2 -= 1

print(result)