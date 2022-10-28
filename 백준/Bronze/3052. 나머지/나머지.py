import sys

div_ls = []
for i in range(10):  
    div_ls.append(int(sys.stdin.readline())%42)

print(len(set(div_ls)))