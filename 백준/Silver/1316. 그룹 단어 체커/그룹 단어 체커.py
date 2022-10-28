import sys

cnt = 0
N = int(sys.stdin.readline())
for i in range(N):  
    word = list(sys.stdin.readline())
    temp_lst = []
    for j in range(len(word)-1):  
        if word[j] != word[j+1]:  
            temp_lst.append(word[j])
    temp_lst.append(word[-1])
    if len(temp_lst) == len(set(temp_lst)):  
        cnt += 1

print(cnt)