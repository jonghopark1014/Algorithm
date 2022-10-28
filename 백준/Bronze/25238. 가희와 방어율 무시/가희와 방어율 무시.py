import decimal
a, b =map(int, input(). split())

if b == 0:  
    if a < 100:
        print(1)
    else:  
        print(0)
else:  
    if a * (100 - b) / 100  < 100:
        print(1)
    else:  
        print(0)