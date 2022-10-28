import sys

T = int(sys.stdin.readline())

for tc in range(1, T+1):
    length, target = map(int, sys.stdin.readline().split())
    lst_N = list(map(int, sys.stdin.readline().split()))
    tmp_N = [i for i in range(length)]
    cnt = 0

    while True:
        max_v = max(lst_N)
        while True:
            if max_v == lst_N[0]:
                a = lst_N.pop(0)
                b = tmp_N.pop(0)
                cnt += 1
                break
            else:
                c = lst_N.pop(0)
                lst_N.append(c)
                d = tmp_N.pop(0)
                tmp_N.append(d)
        if b == target:
            break

    print(cnt)
