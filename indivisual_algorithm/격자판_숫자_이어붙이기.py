T = int(input())

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def dfs(r, c, value):
    global check_lst
    if len(value) == 7:
        check_lst.add(value)
        return
    for i in range(4):
        r2 = r + dr[i]
        c2 = c + dc[i]
        if 0 <= r2 < 4 and 0 <= c2 < 4:
            value += lst_map[r2][c2]
            dfs(r2, c2, value)
            value = value[:len(value)-1]

ans_lst = []

for tc in range(1, T+1):
    lst_map = [list(input().split()) for _ in range(4)]
    check_lst = set()
    for r in range(4):
        for c in range(4):
            dfs(r, c, lst_map[r][c])
    ans_lst.append(f'#{tc} {len(check_lst)}')

print('\n'.join(ans_lst))