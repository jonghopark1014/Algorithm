import sys

T = int(sys.stdin.readline())

for tc in range(1, T+1):  
    R, P = input().split()
    lst_P = list(P)
    int_R = int(R)
    for i in lst_P:  
        print(i * int_R, end = '')
    print()