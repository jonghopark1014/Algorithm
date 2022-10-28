import sys

lst_A = []
lst_B = []
lst_C = []

value = int(sys.stdin.readline())

for i in range(6):
    A, B = map(int, sys.stdin.readline().split())
    lst_C.append(B)
    if A == 1 or A == 2:
        lst_A.append(B)
    else:
        lst_B.append(B)

maxA = max(lst_A)
maxB = max(lst_B)
area = maxA * maxB

lst_A.remove(maxA)
lst_B.remove(maxB)

result_A = 0
result_B = 0
for i in range(len(lst_C)):
    if i == len(lst_C) -1:
        if lst_C[i - 1] in lst_A and lst_C[0] in lst_A:
            result_A = lst_C[i]
        if lst_C[i - 1] in lst_B and lst_C[0] in lst_B:
            result_B = lst_C[i]
    else:
        if lst_C[i-1] in lst_A and lst_C[i+1] in lst_A:
            result_A = lst_C[i]
        if lst_C[i - 1] in lst_B and lst_C[i + 1] in lst_B:
            result_B = lst_C[i]

print((area - result_A * result_B)*value)