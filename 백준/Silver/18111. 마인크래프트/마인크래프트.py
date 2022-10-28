import sys

N, M, B = map(int, sys.stdin.readline().split())
lst_n = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

min_time = 99999999999
max_high = 0

for i in range(0, 257):
    tmp_B = B
    tmp_time = 0
    tmp_high = i
    for r in lst_n:
        for c in r:
            if c > i:
                tmp_time += (c - i) * 2
                tmp_B += c - i
            elif c - i < 0:
                tmp_time += i - c
                tmp_B += c - i
            if min_time < tmp_time:
                break
        if min_time < tmp_time:
            break
    if tmp_B >= 0:
        if min_time >= tmp_time:
            min_time = tmp_time
            max_high = tmp_high

print(min_time, max_high)
