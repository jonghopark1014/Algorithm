import sys
sys.stdin = open('input.txt')

T = int(input())

dic_num = {'0': '0001101', '1':'0011001', '2': '0010011', '3':'0111101', '4':'0100011',
           '5':'0110001', '6':'0101111', '7':'0111011', '8':'0110111', '9':'0001011'}

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = ''
    for i in range(N):
        arr_input = input()
        arr += arr_input
    tmp = ''
    num_lst = []
    while True:
        if len(num_lst) == 8:
            break
        for i in range(len(arr)):
            for j in range(10):
                if arr[i:i+7] == dic_num[str(j)]:
                    tmp = arr[i:i+56]
                    break
            for i in range(0, len(tmp), 7):
                for j in range(10):
                     if tmp[i:i+7] == dic_num[str(j)]:
                        num_lst.append(j)
            if len(num_lst) == 8:
                break
            else:
                num_lst = []

    num = 0
    for i in range(0, len(num_lst), 2):
        num += num_lst[i]
    num *= 3
    for j in range(1, len(num_lst), 2):
        num += num_lst[j]

    if num % 10 == 0 and len(num_lst) == 8:
        print(f'#{tc}', sum(num_lst))
    else:
        print(f'#{tc}', 0)