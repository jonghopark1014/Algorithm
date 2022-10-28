import sys

N = int(sys.stdin.readline())
lst_N = [0] * (10000+2)

for i in range(N):  
    num = int(sys.stdin.readline()) 
    lst_N[num] += 1

for j in range(len(lst_N)):  
    if lst_N[j] != 0:  
        for k in range(lst_N[j]):
            sys.stdout.write(str(j)+'\n')
