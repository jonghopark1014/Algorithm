import sys

input_read = sys.stdin.readline

N, M = map(int, input_read().split())

print(N * M - 1)