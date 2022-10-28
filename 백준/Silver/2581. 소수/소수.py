import sys

def isPrime(x):
    global prime_lst
    if x > 1:
        if x == 2 or x == 3:
            prime_lst += [x]
        else:
            if x % 2 != 0:
                for i in range(2, x // 2 + 1):
                    if x % i == 0:
                        break
                else:
                    prime_lst += [x]

prime_lst = []
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())

for num in range(A, B+1):
    isPrime(num)
if len(prime_lst) > 0:
    print(sum(prime_lst))
    print(prime_lst[0])
else:
    print(-1)
