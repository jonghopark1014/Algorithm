# def Quick_sort(lst, l, r):
#     if l < r:
#         s = partition(lst, l, r)
#         Quick_sort(lst, l, s - 1)
#         Quick_sort(lst, s+1, r)
#     return lst
#
# def partition(lst, p, r):
#     x = lst[r]
#     i = p - 1
#     for j in range(p, r):
#         if lst[j] <= x:
#             i += 1
#             lst[i], lst[j] = lst[j], lst[i]
#     lst[i+1], lst[r] = lst[r], lst[i+1]
#     return i + 1
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     lst_N = list(map(int, input().split()))
#     print(f'#{tc}', Quick_sort(lst_N, 0, N-1)[N//2])

def Quick_sort(lst, l, r):
    if l < r:
        s = partition2(lst, l, r)
        Quick_sort(lst, l, s)
        Quick_sort(lst, s + 1, r)
    return lst

def partition2(lst, l, r):
    x = lst[(l+r) // 2]
    i, j = l, r

    while True:
        while i <= j and lst[i] < x:
            i += 1
        while i <= j and lst[j] > x:
            j -= 1
        if i >= j:
            break
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1

    lst[l], lst[j] = lst[j], lst[l]
    return j

for tc in range(1, int(input()) + 1):
    N = int(input())
    lst_N = list(map(int, input().split()))
    print(f'#{tc}', Quick_sort(lst_N, 0, N-1)[N//2])
