from collections import deque

def merge_sort(lst):
    global cnt
    if len(lst) < 2:
        return lst

    mid = len(lst) // 2
    L = merge_sort(lst[:mid])
    R = merge_sort(lst[mid:])

    if L[-1] > R[-1]:
        cnt += 1
    tmp_lst = []
    l = r = 0
    while l < len(L) and r < len(R):
        if L[l] < R[r]:
            tmp_lst.append(L[l])
            l += 1
        else:
            tmp_lst.append(R[r])
            r += 1
    tmp_lst += L[l:]
    tmp_lst += R[r:]

    return tmp_lst

ans_lst = []
for tc in range(1, int(input())+1):
    N = int(input())
    cnt = 0
    lst_N = merge_sort(list(map(int, input().split())))
    ans_lst.append(f'#{tc} {lst_N[N//2]} {cnt}')

print('\n'.join(ans_lst))

