import sys

lst_n = [int(sys.stdin.readline()) for i in range(9)]

for i in range(len(lst_n)-1):
    for j in range(i+1, len(lst_n)):
        a = lst_n[i]
        b = lst_n[j]
        if sum(lst_n) - a - b == 100:
            break
    if sum(lst_n) - a - b == 100:
        lst_n.remove(a)
        lst_n.remove(b)
        break



for i in sorted(lst_n):
    print(i)