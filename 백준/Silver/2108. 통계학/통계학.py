import sys

N = int(sys.stdin.readline())
lst_N = sorted([int(sys.stdin.readline()) for _ in range(N)])

dic_N = {}
for i in lst_N:
    if i in dic_N:
        dic_N[i] += 1
    else:
        dic_N[i] = 1

max_lst = []
for idx, value in dic_N.items():
    if max(dic_N.values()) == value:
        max_lst.append(idx)
max_lst.sort()



print(int(round(sum(lst_N)/N, 0)))
print(lst_N[N//2])
if len(max_lst) > 1:
    print(max_lst[1])
else:
    print(*max_lst)
print(lst_N[-1]-lst_N[0])