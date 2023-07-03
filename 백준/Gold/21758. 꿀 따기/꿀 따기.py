import sys

input_read = sys.stdin.readline

#input
N = int(input_read())
arr = list(map(int, input_read().split()))
sum_arr = [arr[0]]
for i in range(1, N):
    sum_arr.append(arr[i] + sum_arr[i - 1])

ans = 0

# CASE 1 (벌벌통)
## 벌1 = 0 / 통 = N - 1
### 1번 벌 계산
for two in range(1, N - 1):
    bee_one = sum_arr[-1] - arr[0] - arr[two]
    bee_two = sum_arr[-1] - sum_arr[two]
    ans = max(ans, bee_one + bee_two)

# CASE 2 (통벌벌)
## 통 = 0 / 벌2 = N - 1
for one in range(N - 2, 0, -1):
    bee_two = sum_arr[-1] - arr[-1] - arr[one]
    bee_one = sum_arr[one - 1]
    ans = max(ans, bee_one + bee_two)

# CASE 3 (벌통벌)
## 벌1 = 0 / 벌2 = N - 1
for basket in range(1, N - 1):
    bee_one = sum_arr[basket] - arr[0]
    bee_two = sum_arr[-1] - sum_arr[basket - 1] - arr[-1]
    ans = max(ans, bee_one + bee_two)

print(ans)