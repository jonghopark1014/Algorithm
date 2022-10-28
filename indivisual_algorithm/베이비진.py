T = int(input())

tmp_lst = []
def triple(lst, turn):
    global ans
    if turn == 0:
        cnt = -1
    else:
        cnt = 0
    dic_num = {}
    for i in range(len(lst)):
        if lst[i] not in dic_num:
            dic_num[lst[i]] = 1
        else:
            dic_num[lst[i]] += 1
        cnt += 2
        if dic_num[lst[i]] == 3:
            return cnt
        if cnt > ans:
            return 99999
    else:
        return 99999


def runrun(lst, turn):
    global ans
    if turn == 0:
        cnt = 3
    else:
        cnt = 4
    for i in range(2, len(lst)):
        cnt += 2
        if cnt > ans:
            return 99999
        if lst[i] - 1 in lst[:i]:
            if lst[i] - 2 in lst[:i] or lst[i] + 1 in lst[:i]:
                return cnt
        elif lst[i] + 1 in lst[:i]:
            if lst[i] + 2 in lst[:i]:
                return cnt

    else:
        return 99999

lst_all = [list(map(int, input().split())) for _ in range(T)]
tc = 0
for lst_al in lst_all:
    tc += 1
    one = [lst_al[i] for i in range(0, len(lst_al), 2)]
    two = [lst_al[i] for i in range(1, len(lst_al), 2)]
    ans = 99999
    one_run, one_triple = runrun(one, 0), triple(one, 0)
    if one_run < one_triple:
        ans = one_run
    else:
        ans = one_triple
    winner = 1
    two_run, two_triple = runrun(two, 1), triple(two, 1)
    if two_run < two_triple:
        ans2 = two_run
    else:
        ans2 = two_triple

    if ans > ans2:
        ans = ans2
        winner = 2

    if ans == 99999:
        tmp_lst.append(f'#{tc} {0}')
    else:
        tmp_lst.append(f'#{tc} {winner}')

print('\n'.join(tmp_lst))