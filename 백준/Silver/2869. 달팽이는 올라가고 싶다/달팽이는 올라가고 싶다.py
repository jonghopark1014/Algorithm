import sys

A, B, V = map(int, sys.stdin.readline().split())
day_cnt = 0

if V - A == 0:
    day_cnt = 1
else:
    if (V-A) % (A-B) != 0:
        day_cnt = (V - A) // (A - B) + 2
    else:
        day_cnt = (V - A) // (A - B) + 1

print(day_cnt)