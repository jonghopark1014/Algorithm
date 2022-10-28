import sys

T = int(input())
for tc in range(1, T+1):  
    ox = sys.stdin.readline()
    ox_lst = ox.replace('X', ' ').split()
    sum = 0
    for i in ox_lst:  
        for j in range(1, len(i)+1):  
            sum += j
    
    print(sum)