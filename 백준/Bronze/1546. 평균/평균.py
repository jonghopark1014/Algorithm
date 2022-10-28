N = int(input())

ls_point = list(map(int, input().split()))

point_max = max(ls_point)
re_ls = []

for i in range(N):  
    re_ls.append(ls_point[i]/point_max*100)
point_avg = sum(re_ls) / len(re_ls)

print(point_avg)