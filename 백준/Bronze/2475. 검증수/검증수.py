import sys

N = list(sys.stdin.readline().split())

for i in range(len(N)):
    N[i] = int(N[i]) ** 2

print(sum(N) % 10)
