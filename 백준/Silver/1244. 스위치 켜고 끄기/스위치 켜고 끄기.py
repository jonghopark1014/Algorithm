import sys

def switchProgram(a, b):
    global switch, switch_lst
    if a == 1:
        x = switch // b
        for i in range(1, x+1):
            if switch_lst[b * i] == 1:
                switch_lst[b * i] = 0
            else:
                switch_lst[b * i] = 1
    else:
        if b < 2 or b > switch -1:
            if switch_lst[b] == 1:
                switch_lst[b] = 0
            else:
                switch_lst[b] = 1
        else:
            c = 0
            while True:
                c += 1
                if b+c > switch or b-c < 1:
                    c -= 1
                    break
                elif switch_lst[b-c] != switch_lst[b+c]:
                    c -= 1
                    break
            for i in range(b-c, b+c+1):
                if switch_lst[i] == 1:
                    switch_lst[i] = 0
                else:
                    switch_lst[i] = 1


switch = int(sys.stdin.readline())
switch_lst = [99] + list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())
lst_n = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in lst_n:
    switchProgram(i[0], i[1])

if switch > 20:
    for i in range(1, len(switch_lst)):
        print(switch_lst[i], end = ' ')
        if i % 20 == 0:
            print()
else:
    print(*switch_lst[1:])
