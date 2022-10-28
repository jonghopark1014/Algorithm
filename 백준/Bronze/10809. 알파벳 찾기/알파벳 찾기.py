import sys

word_lst = list(sys.stdin.readline().strip())

# ord 아스키코드 변환 소문자a == 97
n_lst = [-1] * 26

for i in range(len(word_lst)):  
    if n_lst[ord(word_lst[i])-97] == -1:
        n_lst[ord(word_lst[i])-97] = i
print(*n_lst)