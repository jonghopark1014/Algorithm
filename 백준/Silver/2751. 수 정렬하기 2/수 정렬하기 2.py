import sys

N = int(sys.stdin.readline())

lst_N = sorted([int(sys.stdin.readline()) for _ in range(N)])

for i in lst_N:  
    print(i)