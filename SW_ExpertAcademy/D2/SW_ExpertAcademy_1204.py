T = int(input())

for tc in range(1, T+1):  
    test = int(input())
    ls_point = list(map(int, input().split()))
    dic_point = {}

    for i in ls_point:  
        if i in dic_point:  
            dic_point[i] += 1
        else:  
            dic_point[i] = 1

    max_point = max(dic_point, key=dic_point.get)

    print(f'#{test} {max_point}')