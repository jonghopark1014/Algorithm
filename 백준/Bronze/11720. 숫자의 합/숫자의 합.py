import sys

N = int(sys.stdin.readline())
lst_N = list(sys.stdin.readline().strip())

sum_N = 0
for i in lst_N:  
    sum_N += int(i)

print(sum_N)