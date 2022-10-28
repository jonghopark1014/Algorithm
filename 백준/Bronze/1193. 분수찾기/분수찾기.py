import sys

N = int(sys.stdin.readline())

sumI = 0
for i in range(1, 10000000):
    num = i
    sumI += i
    if N <= sumI:
        break

if num % 2== 0:
    print(f'{num-sumI+N}/{1+sumI-N}')
else:
    print(f'{1 + sumI - N}/{num - sumI + N}')