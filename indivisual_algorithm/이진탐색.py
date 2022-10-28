def Quick_sort(lst, l, r):
    if l < r:
        s = partition(lst, l, r)
        Quick_sort(lst, l, s - 1)
        Quick_sort(lst, s + 1, r)
    return lst

def partition(lst, p, r):
    x = lst[r]
    i = p - 1
    for j in range(p, r):
        if lst[j] <= x:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[r] = lst[r], lst[i+1]
    return i + 1

ans_lst = []

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    lst_N = list(map(int, input().split()))
    lst_M = list(map(int, input().split()))
    Quick_sort(lst_N, 0, N-1)
    cnt = 0
    for i in lst_M:
        l = 0
        r = N - 1
        mid = (N-1) // 2
        pre_v = 9 # 0 - l 1 - r
        while l <= r:
            if lst_N[mid] > i:
                r = mid - 1
                mid = (l + r) // 2
                if pre_v == 1:
                    break
                pre_v = 1
            elif lst_N[mid] < i:
                l = mid + 1
                mid = (l + r) // 2
                if pre_v == 0:
                    break
                pre_v = 0
            elif lst_N[mid] == i:
                cnt += 1
                break

    ans_lst.append(f'#{tc} {cnt}')

print('\n'.join(ans_lst))

'''
재귀
def binary(l, r, dir, i):
    global cnt
    n = (l + r) // 2
    if i == A[n]:
        cnt += 1
    elif i < A[n]:
        if dir == 'l':
            return
        else:
            dir = 'l'
            binary(l, n-1, dir, i)
    elif i > A[n]:
        if dir == 'r':
            return
        else:
            dir = 'r'
            binary(n + 1, r, dir, i)


for TC in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    arr = list(map(int, input().split()))
    cnt = 0
    for i in arr:
        binary(0, len(A) - 1, 0, i)
    print(f'#{TC} {cnt}')
'''