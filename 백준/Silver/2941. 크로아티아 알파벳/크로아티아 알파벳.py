import sys

S = sys.stdin.readline().strip()

cro_lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
cnt2 = 0
cnt3 = 0
left, right = 0, 2
while right <= len(S):  
    if S[left:right] in cro_lst:  
        cnt += 1
        cnt2 += 1
        left = right
        right += 2
    elif S[left:right+1] in cro_lst:  
        cnt += 1
        cnt3 += 1
        left = right + 1
        right += 3
    else:  
        left += 1
        right += 1

result = cnt + len(S) - 3 * cnt3 - 2 * cnt2
print(result)