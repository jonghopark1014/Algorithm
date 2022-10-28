import sys

word = list(sys.stdin.readline().strip())

for i in word:  
    if i.islower() == True:  
        print(i.upper(), end = '')
    elif i.isupper() == True:  
        print(i.lower(), end='')
