import sys

def prime_lst(a, b):
    a += 1
    TF_lst = [True] * (b+1)
    m = int(b**0.5)
    for i in range(2, m+1):
        if TF_lst[i] == True:
            for j in range(i+i, b+1, i):
                TF_lst[j] = False
    return [i for i in range(a, b+1) if TF_lst[i] == True]

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        print(len(prime_lst(n, 2*n)))