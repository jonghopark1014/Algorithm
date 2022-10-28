import sys
N = sys.stdin.readline().split()
A, B = int(N[0][::-1]), int(N[1][::-1])

if A > B:  
    print(A)
else:  
    print(B)