
for i in range(1, int(input())+1):  
    a = [w for w in input()]
    if a == a[::-1]:  
        print(f"#{i} {1}")
    else:  
        print(f"#{i} {0}")
