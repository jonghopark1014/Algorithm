T = int(input())

for tc in range(1, T+1):  
    text = input()
    text_ls = []
    for i in range(11):  
        if text[0:i] == text[i : 2*i]:  
            text_ls.append(text[0:i])
    print(f'#{tc} {len(text_ls[1])}')