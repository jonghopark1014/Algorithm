import sys
N = int(sys.stdin.readline())
count_han = 0
for i in range(1, N+1):  
    if i < 100:  
        count_han += 1
    elif i < 1000:  
        re_lst = list(str(i))
        if int(re_lst[0]) - int(re_lst[1]) == int(re_lst[1]) - int(re_lst[2]):  
            count_han += 1

print(count_han)  
