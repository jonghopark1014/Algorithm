import sys

def Isprime(k):
    if k > 1:
        if k == 2 or k == 3:
            return 1
        else:
            for i in range(2, k//2+1):
                if k % i == 0:
                    return 0
            return 1
    else:
        return 0



N = int(sys.stdin.readline())
lst_N = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in lst_N:
    cnt += Isprime(i)

print(cnt)