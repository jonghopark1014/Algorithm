import sys

N = sys.stdin.readline().strip()
print(''.join(sorted(N, reverse=True)))