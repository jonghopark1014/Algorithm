N_list = [i for i in range(1, 10000)]

re_list = []
for i in N_list:  
    sum_i = sum(list(map(int, list(str(i)))))
    re_list.append(i+sum_i)

for j in range(1, 10000):  
    if j not in re_list:  
        print(j)