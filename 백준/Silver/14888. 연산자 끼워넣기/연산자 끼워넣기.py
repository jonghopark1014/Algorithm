import sys

def dfs(idx, sum_v, p, m, mul, d):
    global max_v, min_v, plus, minus, multi, divide
    if idx == N - 1:
        max_v = max(sum_v, max_v)
        min_v = min(sum_v, min_v)
        return
    if p < plus:
        dfs(idx + 1, sum_v + lst_N[idx + 1], p + 1, m, mul, d)
    if m < minus:
        dfs(idx + 1, sum_v - lst_N[idx + 1], p, m + 1, mul, d)
    if mul < multi:
        dfs(idx + 1, sum_v * lst_N[idx + 1], p, m, mul + 1, d)
    if d < divide:
        if sum_v / lst_N[idx + 1] < 0 and sum_v % lst_N[idx + 1]:
            dfs(idx + 1, (sum_v // lst_N[idx + 1]) + 1, p, m, mul, d + 1)
        else:
            dfs(idx + 1, sum_v // lst_N[idx + 1], p, m, mul, d + 1)


N = int(sys.stdin.readline())
lst_N = list(map(int, sys.stdin.readline().split()))
plus, minus, multi, divide = map(int, sys.stdin.readline().split())
max_v, min_v = -(10 ** 8), 10 ** 8

dfs(0, lst_N[0], 0, 0, 0, 0)

print(max_v)
print(min_v)
