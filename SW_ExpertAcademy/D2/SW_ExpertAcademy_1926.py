N = int(input())

ls_N = list(map(list, map(str, list(range(1, N+ 1)))))


for i in ls_N:   
    if '3' in i or '6' in i or '9' in i:  
        count = 0
        for j in range(len(i)):  
            if i[j] in '369':  
                count += 1
        print('-' * count, end = ' ')
    else:  
        print(''.join(i), end = ' ')
