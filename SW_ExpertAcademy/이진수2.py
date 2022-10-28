T = int(input())

for tc in range(1, T+1):
    N = float(input())
    bin = ''
    while True:
        N = N * 2
        if N > 1:
            N -= 1
            bin += '1'
        elif N < 1:
            bin += '0'
        else:
            bin += '1'
            break
    if len(bin) > 12:
        print(f'#{tc}', 'overflow')
    else:
        print(f'#{tc}', bin)