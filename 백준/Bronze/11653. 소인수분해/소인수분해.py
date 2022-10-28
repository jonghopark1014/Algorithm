import sys

num = int(sys.stdin.readline())

if num !=1:
    while True:
        for i in range(2, num+1):
            if num % i == 0:
                num = num // i
                print(i)
                break
        if num == 1:
            break