import sys
N = list(sys.stdin.readline().strip())

dic_N = {'1': [], '2': [], '3':['A', 'B', 'C'], '4':['D', 'E', 'F'], '5':['G', 'H', 'I'], '6':['J', 'K', 'L'], '7':['M', 'N', 'O'], '8':['P', 'Q', 'R', 'S'], '9':['T', 'U', 'V'], '10':['W', 'X', 'Y', 'Z']}

sumV = 0
for idx, value in dic_N.items():  
    for i in N:  
        if i in value:  
            sumV += int(idx)

print(sumV)