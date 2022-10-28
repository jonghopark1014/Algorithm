T = int(input())

tmp_lst = []
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    stuck = list(map(int, input().split()))
    weight.sort(reverse=True)
    stuck.sort(reverse=True)
    ans = 0
    idx = 0

    for i in stuck:
        for j in range(idx, len(weight)):
            if i >= weight[j]:
                ans += weight[j]
                idx = j + 1
                break
    tmp_lst.append(f'#{tc} {ans}')

print('\n'.join(tmp_lst))