def dfs(value, level, Plus, Minus, Multi, Divi):
    global tmp_min, tmp_max
    if level == N - 1:
        if value > tmp_max:
            tmp_max = value
        if value < tmp_min:
            tmp_min = value
        return
    if Plus < plus:
        dfs(value + num_lst[level + 1], level + 1, Plus+1, Minus, Multi, Divi)
    if Minus < minus:
        dfs(value - num_lst[level + 1], level + 1, Plus, Minus + 1, Multi, Divi)
    if Multi < multi:
        dfs(value * num_lst[level + 1], level + 1, Plus, Minus, Multi + 1, Divi)
    if Divi < divi:
        if value > 0 or value % num_lst[level + 1] == 0:
            dfs(value // num_lst[level + 1], level + 1, Plus, Minus, Multi, Divi + 1)
        else:
            dfs(value // num_lst[level + 1] + 1, level + 1, Plus, Minus, Multi, Divi + 1)

for tc in range(1, int(input()) + 1):
    tmp_min = 100000000
    tmp_max = -100000000
    N = int(input())
    plus, minus, multi, divi = map(int, input().split())
    num_lst = list(map(int, input().split()))
    dfs(num_lst[0], 0, 0, 0, 0, 0)
    print(f'#{tc}', tmp_max - tmp_min)
