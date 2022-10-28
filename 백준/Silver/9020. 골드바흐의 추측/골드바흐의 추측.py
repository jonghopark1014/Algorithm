import sys

def prime_lst(a, b):
    TF_lst = [True] * (b+1)
    m = int(b**0.5)
    for i in range(2, m+1):
        if TF_lst[i] == True:
            for j in range(i+i, b+1, i):
                TF_lst[j] = False
    return [i for i in range(a, b+1) if TF_lst[i] == True]

T = int(sys.stdin.readline())

lst_prime = prime_lst(2, 10000)
sli_num = 0

for i in range(T):
    N = int(sys.stdin.readline())
    for k in range(N//2+1):
        if N//2-k in lst_prime and N//2+k in lst_prime:
            print(N//2-k, N//2+k)
            break