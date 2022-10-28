T = int(input())

def recursion(s, l, r):
    global cnt
    if l >= r:  return 1
    else:
        if s[l] != s[r]:
            return 0
        else:
            cnt += 1
            return recursion(s, l + 1, r - 1)

def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)

for tc in range(1, T+1):
    a = input()
    cnt = 1
    print(isPalindrome(list(a)), end = ' ')
    print(cnt)