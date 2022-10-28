T = int(input())

for tc in range(1, T+1):  
    list_num = list(map(int, input().split()))
    print(f'#{tc} {len(list_num)} {list_num[-1]}')