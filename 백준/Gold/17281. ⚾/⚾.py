import sys
from itertools import permutations

# input
read_input = sys.stdin.readline

N = int(read_input())
arr = [list(map(int, read_input().split())) for _ in range(N)]

# # player 셋팅을 위한 재귀 (시간초과)
# def recur_player(x):
#     global ans
#
#     if x == 10:
#         point = 0
#         last = 9 - 1
#
#         for j in range(N):
#             out = 0
#             game = [0 for _ in range(8)]
#             while True:
#                 bat = (last + 1) % 9
#                 num = arr[j][player[bat] - 1]
#
#                 if num == 1:
#                     for i in range(3, 0, -1):
#                         game[i + 1] += game[i]
#                         game[i] = 0
#                     game[1] += 1
#                 elif num == 2:
#                     for i in range(3, 0, -1):
#                         game[i + 2] += game[i]
#                         game[i] = 0
#                     game[2] += 1
#                 elif num == 3:
#                     for i in range(3, 0, -1):
#                         game[i + 3] += game[i]
#                         game[i] = 0
#                     game[3] += 1
#                 elif num == 4:
#                     for i in range(3, 0, -1):
#                         game[i + 4] += game[i]
#                         game[i] = 0
#                     game[4] += 1
#                 elif not num:
#                     out += 1
#                     if out == 3:
#                         point += sum(game[4 : 8])
#                         last = bat
#                         break
#                 last = bat
#
#         ans = max(point, ans)
#         return
#
#     for i in range(9):
#         if not player[i]:
#             player[i] = x
#             recur_player(x + 1)
#             player[i] = 0
#
#
# # 기본 플레이어 셋팅
# player = [0 for _ in range(9)]
# player[4 - 1] = 1
#
# # 재귀 + 계산
# ans = 0
# recur_player(2)
#
# print(ans)

# itertools permutation 활용
ans = 0
nums = [i for i in range(2, 10)]
# permutation 모든 조합
p = list(permutations(nums, 8))

# for문 시작 - 모든 순열 순회
for i in p:
    point = 0
    last_player = 9 - 1

    # 이닝만큼 for문
    for j in range(N):
        out = 0
        game = [0 for _ in range(4)]
        b1, b2, b3 = 0, 0, 0
        while True:
            bat = (last_player + 1) % 9
            playing = 0
            if bat < 3:
                playing = arr[j][i[bat] - 1]
            elif bat == 3:
                playing = arr[j][0]
            elif bat > 3:
                playing = arr[j][i[bat - 1] - 1]

            if playing == 1:
                if b3:  
                    point += 1
                b1, b2, b3 = 1, b1, b2
            elif playing == 2:
                if b2 and b3:  
                    point += 2
                elif b2 or b3:  
                    point += 1
                b1, b2, b3 = 0, 1, b1
                
            elif playing == 3:
                if b1:  
                    point += 1
                if b2:  
                    point += 1
                if b3:  
                    point += 1
                b1, b2, b3 = 0, 0, 1
            elif playing == 4:
                point += 1
                if b1:  
                    point += 1
                if b2:  
                    point += 1
                if b3:  
                    point += 1
                b1, b2, b3 = 0, 0, 0
                
            elif not playing:
                out += 1
                if out == 3:
                    last_player = bat
                    break
            last_player = bat

    ans = max(point, ans)

print(ans)




