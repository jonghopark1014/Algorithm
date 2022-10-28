T = int(input())

def highShelf(level, idx):
    global ans, sum_high, max_v
    if sum_high - B > ans:
        return
    elif sum_high >= B:
        ans = min(sum_high - B, ans)
        return
    elif level == N:
        ans = min(sum_high - B, ans)
        return
    elif B > (N - level) * max_v + sum_high:
        return
    for i in range(idx, N):
        if used[i] == 1:
            continue
        used[i] = 1
        sum_high += member_lst[i]
        highShelf(level + 1, i)
        used[i] = 0
        sum_high -= member_lst[i]

ans_lst = []
for tc in range(1, T+1):
    N, B = map(int, input().split())
    member_lst = list(map(int, input().split()))
    member_lst.sort(reverse=True)
    max_v = max(member_lst)
    ans = 99999
    used = [0] * N
    sum_high = 0
    highShelf(0, 0)
    ans_lst.append(f'#{tc} {ans}')

print('\n'.join(ans_lst))