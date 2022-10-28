T = int(input())

ans_lst = []
for tc in range(1, T+1):
    two_num = list(map(int, input()))
    thr_num = list(map(int, input()))
    two_lst = set()
    for i in range(len(two_num)):
        if two_num[i] == 1:
            ten_num = 0
            for j in range(len(two_num)):
                if i != j:
                    ten_num += two_num[j] * (2**(len(two_num) - j - 1))
            two_lst.add(ten_num)
        else:
            ten_num = 0
            for j in range(len(two_num)):
                if i != j:
                    ten_num += two_num[j] * (2 ** (len(two_num) - j - 1))
                else:
                    ten_num += 1 * (2 ** (len(two_num) - j - 1))
            two_lst.add(ten_num)
    len_lst = len(two_lst)

    for a in range(len(thr_num)):
        if thr_num[a] == 2:
            ten_num_2 = 0
            for b in range(len(thr_num)):
                if a != b:
                    ten_num_2 += thr_num[b] * (3**(len(thr_num) - b - 1))
                else:
                    ten_num_2 += 3 ** (len(thr_num) - b - 1)
            two_lst.add(ten_num_2)
            if len_lst == len(two_lst):
                ans_lst.append(f'#{tc} {ten_num_2}')
                break
            else:
                len_lst += 1

            ten_num_2 = 0
            for b in range(len(thr_num)):
                if a != b:
                    ten_num_2 += thr_num[b] * (3 ** (len(thr_num) - b - 1))
            two_lst.add(ten_num_2)
            if len_lst == len(two_lst):
                ans_lst.append(f'#{tc} {ten_num_2}')
                break
            else:
                len_lst += 1

        elif thr_num[a] == 1:
            ten_num_2 = 0
            for b in range(len(thr_num)):
                if a != b:
                    ten_num_2 += thr_num[b] * (3 ** (len(thr_num) - b - 1))
            two_lst.add(ten_num_2)
            if len_lst == len(two_lst):
                ans_lst.append(f'#{tc} {ten_num_2}')
                break
            else:
                len_lst += 1

            ten_num_2 = 0
            for b in range(len(thr_num)):
                if a != b:
                    ten_num_2 += thr_num[b] * (3 ** (len(thr_num) - b - 1))
                else:
                    ten_num_2 += 2 * (3 ** (len(thr_num) - b - 1))
            two_lst.add(ten_num_2)
            if len_lst == len(two_lst):
                ans_lst.append(f'#{tc} {ten_num_2}')
                break
            else:
                len_lst += 1

        elif thr_num[a] == 0:
            ten_num_2 = 0
            for b in range(len(thr_num)):
                if a != b:
                    ten_num_2 += thr_num[b] * (3**(len(thr_num) - b - 1))
                else:
                    ten_num_2 += 3 ** (len(thr_num) - b - 1)
            two_lst.add(ten_num_2)
            if len_lst == len(two_lst):
                ans_lst.append(f'#{tc} {ten_num_2}')
                break
            else:
                len_lst += 1

            ten_num_2 = 0
            for b in range(len(thr_num)):
                if a != b:
                    ten_num_2 += thr_num[b] * (3 ** (len(thr_num) - b - 1))
                else:
                    ten_num_2 += 2 * (3 ** (len(thr_num) - b - 1))
            two_lst.add(ten_num_2)
            if len_lst == len(two_lst):
                ans_lst.append(f'#{tc} {ten_num_2}')
                break
            else:
                len_lst += 1

print('\n'.join(ans_lst))