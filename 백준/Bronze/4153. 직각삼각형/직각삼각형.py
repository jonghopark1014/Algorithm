import sys

a, b, c= 0, 0, 0

while True:  
    a, b, c = sorted(map(int, sys.stdin.readline().split()))
    if a == b == c == 0:  
        break
    if c ** 2 == a **2 + b ** 2:  
        print('right')
    else:  
        print('wrong')