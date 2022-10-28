import sys

x, y = map(int, sys.stdin.readline().split())
# 1 북 2 남 3 서 4 동
store_cnt = int(sys.stdin.readline())
lst_store = [list(map(int, sys.stdin.readline().split())) for _ in range(store_cnt)]
dong, dong_x = map(int, sys.stdin.readline().split())
result = 0

for i in lst_store:
    if i[0] + dong == 2:
        result += abs(i[1] - dong_x)
    elif i[0]+dong == 3:
        if i[1] + dong_x > x:
            result += y + x - i[1] + x - dong_x
        else:
            result += y + i[1] + dong_x
    elif i[0]+dong == 4:
        if dong == 1 or dong == 3:
            result += i[1] + dong_x
        else:
            result += abs(i[1] - dong_x)
    elif i[0] + dong == 5:
        if i[0] == 1:
            result += x - i[1] + dong_x
        elif i[0] == 4:
            result += x + i[1] - dong_x
        elif i[0] == 2:
            result += i[1] + y - dong_x
        elif i[0] == 3:
            result += dong_x + y - i[1]
    elif i[0] + dong == 6:
        if i[0] == 3:
            result += abs(i[1] - dong_x)
        elif i[0] == 2:
            result += x - i[1] + y - dong_x
        else:
            result += y - i[1] + x - dong_x
    elif i[0] + dong == 7:
        if i[1] + dong_x > y:
            result += x + y - i[1] + y - dong_x
        else:
            result += x + i[1] + dong_x
    elif i[0] + dong == 8:
        result += abs(i[1] - dong_x)

print(result)