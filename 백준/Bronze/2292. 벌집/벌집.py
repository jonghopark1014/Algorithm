import sys

N = int(sys.stdin.readline())

num_lst = [1]
i = 0
while num_lst[i]-6 < N:  
    num_lst.append(num_lst[i]+6*(i+1))
    i += 1

for i in range(len(num_lst)-1):  
    if N == 1:  
        print(1)
    elif num_lst[i] < N <= num_lst[i+1]:  
        print(i+2)
