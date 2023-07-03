import sys
from collections import deque

read_input = sys.stdin.readline

# setting
air = deque()
dis_cheese = deque()
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

#input
R, C = map(int, read_input().split())
arr = []
time = 0
cheeses = 0
for r in range(R):
    tmp = list(map(int, read_input().split()))
    for c in range(C):
        if tmp[c]:
            cheeses += 1
    arr.append(tmp)

pre_cheese = cheeses

# dis_cheese : 사라질 치즈 deque / now_cheese : 잔여 치즈
## now_cheese가 있다면 dr, dc 확인 후 하나라도 0이면 dis_cheese에 추가
## dis_cheese pop 하면서 해당 지점 0으로 교체
## 교체 후 시간 올리고 다시 진행

while cheeses:
    visited = [[0 for c in range(C)] for r in range(R)]

    # 공기에서 체크
    air = deque()
    air.append([0, 0])
    visited[0][0] = 1
    while len(air):
        air_info = air.popleft()
        air_r, air_c = air_info[0], air_info[1]
        for i in range(4):
            new_r = air_r + dr[i]
            new_c = air_c + dc[i]
            if 0 <= new_r < R and 0 <= new_c < C and not visited[new_r][new_c]:
                if not arr[new_r][new_c]:
                    air.append([new_r, new_c])
                    visited[new_r][new_c] = 1
                else:
                    dis_cheese.append([new_r, new_c])
                    visited[new_r][new_c] = 1

    # 사라지기
    while len(dis_cheese):
        cheese = dis_cheese.popleft()
        cheese_r, cheese_c = cheese[0], cheese[1]
        arr[cheese_r][cheese_c] = 0
        cheeses -= 1

    time += 1
    if not cheeses:
        break
    else:
        pre_cheese = cheeses

print(time)
print(pre_cheese)