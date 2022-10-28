import sys

N = (sys.stdin.readline().strip()).lower()
lst_N = list(N)


re_lst = list(set(N))
count_lst = []

for i in range(len(re_lst)):  
    count_lst.append(lst_N.count(re_lst[i]))

if count_lst.count(max(count_lst)) != 1:  
    print('?')
else:  
    print(re_lst[count_lst.index(max(count_lst))].upper())