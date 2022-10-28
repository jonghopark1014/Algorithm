import sys

num = int(sys.stdin.readline())

cnt = 999999
temp_cnt = 0
share_fiv = num // 5
share_thr = num // 3
if share_fiv != 0 or share_thr != 0:
    for i in range(1, share_fiv+1):
        if (num - 5*i) % 3 == 0:
            temp_cnt = i + ((num-5*i)//3)
            if temp_cnt < cnt:
                cnt = temp_cnt
        temp_cnt = 0

    for j in range(1, share_thr+1):
        if (num - 3*j) % 5 == 0:
            temp_cnt = j + ((num-3*j)//5)
            if temp_cnt < cnt:
                cnt = temp_cnt
        temp_cnt = 0
else:
    cnt = -1
if cnt == 999999:
    cnt = -1

print(cnt)