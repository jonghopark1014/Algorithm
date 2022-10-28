now_h, now_m = map(int, input().split())
cook_m = int(input())

after_h = now_h+((cook_m+now_m)//60)
after_m = cook_m+now_m-(60*((cook_m+now_m)//60))

if after_h >= 24:  
    after_h = after_h - 24

print(f'{after_h} {after_m}')