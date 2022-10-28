import sys

def prime_lst(a, b):
    if a == 1:
        a += 1
    b += 1
    TF_lst = [True] * b
    m = int(b**0.5)
    for i in range(2, m+1):
        if TF_lst[i] == True:
            for j in range(i+i, b, i):
                TF_lst[j] = False
    return [i for i in range(a, b) if TF_lst[i] == True]

A, B = map(int, sys.stdin.readline().split())

result = prime_lst(A,B)

for i in result:
    print(i)