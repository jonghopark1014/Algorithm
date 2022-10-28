import sys

Al = int(sys.stdin.readline())
Al_lst = list(map(int, sys.stdin.readline().split()))
Al_dic = {}
for i in Al_lst:
    if i in Al_dic:
        Al_dic[i] += 1
    else:
        Al_dic[i] = 1
N = int(sys.stdin.readline())
for i in list(map(int, sys.stdin.readline().split())):
    try:
        print(Al_dic[i], end = ' ')
    except:
        print(0, end = ' ')
