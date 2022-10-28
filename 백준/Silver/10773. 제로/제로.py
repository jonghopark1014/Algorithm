import sys

stack = []

N = int(sys.stdin.readline())

for i in range(N):
    a = int(sys.stdin.readline())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)

print(sum(stack))