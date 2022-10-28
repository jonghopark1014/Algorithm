import sys

ls_n = []
for i in range(9):  
    ls_n.append(int(sys.stdin.readline()))

print(max(ls_n))
print(ls_n.index(max(ls_n))+1)