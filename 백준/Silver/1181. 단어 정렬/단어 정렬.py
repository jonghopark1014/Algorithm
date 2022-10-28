import sys

N = int(sys.stdin.readline())
lst_N = []
for i in range(N):
    word = sys.stdin.readline().strip()
    if word not in lst_N:
        lst_N.append(word)
lst_N.sort()
lst_N.sort(key=len)

for i in lst_N:
    print(i)