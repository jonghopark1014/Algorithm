def block(r, c):  
    global N, M, res
    tmp_lst = []

    if c + 3 < M:  
        tmp1 = arr[r][c] + arr[r][c + 1] + arr[r][c + 2] + arr[r][c + 3]
        tmp_lst.append(tmp1)
    if r + 3 < N:  
        tmp2 = arr[r][c] + arr[r + 1][c] + arr[r + 2][c] + arr[r + 3][c]
        tmp_lst.append(tmp2)
    if r + 1 < N and c + 1 < M:  
        tmp3 = arr[r][c] + arr[r + 1][c] + arr[r][c + 1] + arr[r + 1][c + 1]
        tmp_lst.append(tmp3)
    if r + 2 < N and c + 1 < M:  
        tmp4 = arr[r][c] + arr[r + 1][c] + arr[r + 2][c] + arr[r + 2][c + 1]
        tmp_lst.append(tmp4)
    if r + 1 < N and c + 2 < M:  
        tmp5 = arr[r][c] + arr[r + 1][c] + arr[r][c + 1] + arr[r][c + 2]
        tmp_lst.append(tmp5)
    if r + 2 < N and c + 1 < M:  
        tmp6 = arr[r][c] + arr[r][c + 1] + arr[r + 1][c + 1] + arr[r + 2][c + 1]
        tmp_lst.append(tmp6)
    if 0 <= r - 1 and c + 2 < M:  
        tmp7 = arr[r][c] + arr[r][c + 1] + arr[r][c + 2] + arr[r - 1][c + 2]
        tmp_lst.append(tmp7)
    if 0 <= r - 2 and c + 1 < M:  
        tmp8 = arr[r][c] + arr[r][c + 1] + arr[r - 1][c + 1] + arr[r - 2][c + 1]
        tmp_lst.append(tmp8)
    if r + 1 < N and c + 2 < M:  
        tmp9 = arr[r][c] + arr[r + 1][c] + arr[r + 1][c + 1] + arr[r + 1][c + 2]
        tmp_lst.append(tmp9)
    if r + 2 < N and c + 1 < M:  
        tmp10 = arr[r][c] + arr[r][c + 1] + arr[r + 1][c] + arr[r + 2][c]
        tmp_lst.append(tmp10)
    if r + 1 < N and c + 2 < M:   
        tmp11 = arr[r][c] + arr[r][c + 1] + arr[r][c + 2] + arr[r + 1][c + 2]
        tmp_lst.append(tmp11)
    if r + 2 < N and c + 1 < M:  
        tmp12 = arr[r][c] + arr[r + 1][c] + arr[r + 1][c + 1] + arr[r + 2][c + 1]
        tmp_lst.append(tmp12)
    if 0 <= r - 1 and c + 2 < M:  
        tmp13 = arr[r][c] + arr[r][c + 1] + arr[r - 1][c + 1] + arr[r - 1][c + 2]
        tmp_lst.append(tmp13)
    if r + 2 < N and 0 <= c - 1:  
        tmp14 = arr[r][c] + arr[r + 1][c] + arr[r + 1][c - 1] + arr[r + 2][c - 1]
        tmp_lst.append(tmp14)
    if r + 1 < N and c + 2 < M:  
        tmp15 = arr[r][c] + arr[r][c + 1] + arr[r + 1][c + 1] + arr[r + 1][c + 2]
        tmp_lst.append(tmp15)
    if 0 <= r - 1 and c + 2 < M:  
        tmp16 = arr[r][c] + arr[r][c + 1] + arr[r - 1][c + 1] + arr[r][c + 2]
        tmp_lst.append(tmp16)
    if 0 <= r - 1 and r + 1 < N and c + 1 < M:  
        tmp17 = arr[r][c] + arr[r][c + 1] + arr[r - 1][c + 1] + arr[r + 1][c + 1]
        tmp_lst.append(tmp17)
    if r + 1 < N and c + 2 < M:  
        tmp18 = arr[r][c] + arr[r][c + 1] + arr[r][c + 2] + arr[r + 1][c + 1]
        tmp_lst.append(tmp18)
    if 0 <= r - 1 and r + 1 < N and c + 1 < M:  
        tmp19 = arr[r][c] + arr[r - 1][c] + arr[r + 1][c] + arr[r][c + 1]
        tmp_lst.append(tmp19)
    
    if len(tmp_lst):  
        res = max(res, max(tmp_lst))

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

res = 0

for r in range(N):  
    for c in range(M):  
        block(r, c)

print(res)