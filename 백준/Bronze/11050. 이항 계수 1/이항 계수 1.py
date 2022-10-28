import sys
N, K = map(int, sys.stdin.readline().split())

def Facto(num):  
    nums = 1
    for i in range(1, num+1):  
        nums *= i 
    return nums


print(int(Facto(N)/(Facto(K)*Facto(N-K))))