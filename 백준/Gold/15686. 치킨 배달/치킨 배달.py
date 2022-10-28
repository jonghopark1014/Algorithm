import sys

def chicRoad(idx, cnt):
    global ans
    r, c = chic_lst[idx][0], chic_lst[idx][1]
    for i in range(len(house_lst)):
        value_lst[i].append(abs(house_lst[i][0] - r) + abs(house_lst[i][1] - c))
    if cnt == M:
        tmp_ans = 0
        for i in value_lst:
            tmp_ans += min(i)
        ans = min(ans, tmp_ans)
        return
    for i in range(idx + 1, len(chic_lst)):
        chicRoad(i, cnt + 1)
        for j in range(len(house_lst)):
            value_lst[j].pop()

N, M = map(int, sys.stdin.readline().split())
lst_N = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
chic_lst = []
house_lst = []

for r in range(N):
    for c in range(N):
        if lst_N[r][c] == 2:
            chic_lst.append([r, c])
        elif lst_N[r][c] == 1:
            house_lst.append([r, c])

ans = 99999999
for i in range(len(chic_lst) - M + 1):
    value_lst = [[] for _ in range(len(house_lst))]
    chicRoad(i, 1)

print(ans)

