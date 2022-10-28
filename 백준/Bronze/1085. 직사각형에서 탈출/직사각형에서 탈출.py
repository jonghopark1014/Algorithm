import sys

a, b = 0, 0
x, y, w, h = map(int, sys.stdin.readline().split())

print(min([x-a, y-b, w-x, h-y]))