# 테스트 케이스
T = int(input())

for tc in range(1, T+1):  
    n = input()
    year = n[:4]
    month = n[4:6]
    day = n[6:]
    if month == '01' or month == '03' or month == '05' or month == '07' or month == '08' or month == '10' or month == '12' :  
        if int(day) <= 31:  
            print(f'#{tc} {year}/{month}/{day}')
        else:  
            print(f'#{tc} -1')
    elif month == '04' or month == '06' or month == '09' or month == '11':  
        if int(day) <= 30:  
            print(f'#{tc} {year}/{month}/{day}')
        else:  
            print(f'#{tc} -1')
    elif month == '02':  
        if int(day) <= 28:  
            print(f'#{tc} {year}/{month}/{day}')
        else:  
            print(f'#{tc} -1')
    else:  
        print(f'#{tc} -1')