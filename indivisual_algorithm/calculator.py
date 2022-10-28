import sys
sys.stdin = open("input_calculator.txt")

def icp(x):
    if x == '*' or x =='/':
        return 2
    elif x == '+' or x == '-':
        return 1
    elif x == '(':
        return 3

def isp(x):
    if x == '*' or x == '/':
        return 2
    elif x == '+' or x == '-':
        return 1
    elif x == '(':
        return 0

for tc in range(1, 11):
    N = int(input())
    lst_N = list(input())
    stack_num = []
    stack_sign = []
    for i in range(N):
        if lst_N[i] == '(' or lst_N[i] == ')' or lst_N[i] == '*' or lst_N[i] == '+' or lst_N[i] == '-' or lst_N[i] == '/':
            if len(stack_sign) == 0:
                stack_sign.append(lst_N[i])
            else:
                if lst_N[i] == ')':
                    while stack_sign[-1] != '(':
                        a = stack_sign.pop()
                        stack_num.append(a)
                    stack_sign.pop()
                else:
                    while stack_sign and icp(lst_N[i]) <= isp(stack_sign[-1]) :
                        a = stack_sign.pop()
                        stack_num.append(a)
                    stack_sign.append(lst_N[i])
        else:
            stack_num.append(lst_N[i])
    while len(stack_sign) != 0:
        a = stack_sign.pop()
        stack_num.append(a)

    stack2_num = []
    for i in range(len(stack_num)):
        if stack_num[i] == '*' or stack_num[i] == '+' or stack_num[i] == '-' or stack_num[i] == '/':
            b = int(stack2_num.pop())
            a = int(stack2_num.pop())
            if stack_num[i] == '*':
                stack2_num.append(a*b)
            elif stack_num[i] == '+':
                stack2_num.append(a + b)
            elif stack_num[i] == '-':
                stack2_num.append(a - b)
            elif stack_num[i] == '/':
                stack2_num.append(a / b)
        else:
            stack2_num.append(stack_num[i])
    print(f'#{tc} {stack2_num[0]}')
