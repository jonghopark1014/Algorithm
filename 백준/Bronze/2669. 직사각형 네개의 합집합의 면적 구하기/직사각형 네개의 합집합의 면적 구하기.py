import sys

used_area = []

for i in range(4):
    a, b, c, d = map(int, sys.stdin.readline().split())
    for j in range(a, c):
        for k in range(b, d):
            if [j, k]  not in used_area:
                used_area.append([j, k])

print(len(used_area))