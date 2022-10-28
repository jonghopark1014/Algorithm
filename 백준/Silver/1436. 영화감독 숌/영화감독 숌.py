import sys

n = int(sys.stdin.readline())

lst_N = [0]

for i in range(1, int(str(n) + '666')):
    if '666' in str(i):
        lst_N.append(i)

print(lst_N[n])