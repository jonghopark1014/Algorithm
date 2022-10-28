import sys
sys.stdin = open('sample_input (7).txt')

T = int(input())

dic_num = {
    '211': 0, '221': 1, '122': 2, '411': 3,
    '132': 4, '231': 5, '114': 6, '312': 7,
    '213': 8, '112': 9
}

dic_num2 = {
    '3211': 0, '2221': 1, '2122': 2, '1411': 3,
    '1132': 4, '1231': 5, '1114': 6, '1312': 7,
    '1213': 8, '3112': 9
}

hexa_bin = {
    '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110',
    '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100',
    'D':'1101', 'E':'1110', 'F':'1111', '0':'0000'
}
for tc in range(1, T+1):
    N, M = map(int, input().split())
    bin_change = []
    for i in range(N):
        a = input().strip()
        num = ''
        for i in range(len(a)):
            num += hexa_bin[a[i]]
        st_num = num.strip('0')
        if st_num != '':
            bin_change.append(st_num + '0')
    bin_change = list(set(bin_change))
    tmp_lst = []
    for i in bin_change:
        j = 0
        num = []
        zero = 1
        one = 1
        while True:
            j += 1
            if j > len(i) -1:
                break
            if i[j] == i[j-1] == '1':
                one += 1
            elif i[j] == '1' and i[j] != i[j-1]:
                num.append(str(zero))
                zero = 1
            elif i[j] == i[j-1] == '0':
                zero += 1
            elif i[j] == '0' and i[j] != i[j-1]:
                num.append(str(one))
                one = 1
            if len(num) == 31:
                tmp_lst.append(num)
                num = []
                while True:
                    j += 1
                    if j > len(i) - 1 or i[j] == '1':
                        one = 1
                        zero = 1
                        break

    tmp_lst3 = list(set([tuple(i) for i in tmp_lst]))
    tmp_lst3 = [list(i) for i in tmp_lst3]
    tmp_lst2 = []
    for i in tmp_lst3:
        if sum(map(int, i[0:3])) > 6:
            a, b, c = map(int, i[0:3])
            yeah = min(a, b, c)
            for j in range(len(i)):
                i[j] = str(int(i[j]) // yeah)
            tmp_lst2.append(''.join(i))
        else:
            tmp_lst2.append(''.join(i))

    total_sum = 0

    for i in tmp_lst3:
        sum_a = 0
        sum_b = 0
        # if sum(map(int, i[0:3])) > 6:
        #     a, b, c = map(int, i[0:3])
        #     yeah = min(a, b, c)
        #     tmp_num = ''
        #     for idx in range(0, 3):
        #         tmp_num += str(int(i[idx])//yeah)
        #     sum_a += dic_num[tmp_num]
        #     cnt = 0
        #     for j in range(3, len(i), 4):
        #         cnt += 1
        #         tmp_num2 = ''
        #         for idx in range(4):
        #             tmp_num2 += str(int(i[j+idx])//yeah)
        #         if cnt % 2 == 1:
        #             sum_b += dic_num2[tmp_num2]
        #         else:
        #             sum_a += dic_num2[tmp_num2]
        #     if (3 * sum_a + sum_b) % 10 == 0:
        #         total_sum += sum_a + sum_b
        # else:
        tmp_num = ''
        for idx in range(0, 3):
            tmp_num += i[idx]
        sum_a += dic_num[tmp_num]
        cnt = 0
        for j in range(3, len(i), 4):
            cnt += 1
            tmp_num2 = ''
            for idx in range(4):
                tmp_num2 += i[j + idx]
            if cnt % 2 == 1:
                sum_b += dic_num2[tmp_num2]
            else:
                sum_a += dic_num2[tmp_num2]
        if (3 * sum_a + sum_b) % 10 == 0:
            total_sum += sum_a + sum_b

    print(f'#{tc}', total_sum)