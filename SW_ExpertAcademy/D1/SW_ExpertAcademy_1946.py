# 케이스 받기
T = int(input())

# 텍스트 나열
for testcase in range(1, T+1):  
    N = int(input())
    text = ''
    for a in range(N):  
        Ci, Ki = input().split()
        text += Ci * int(Ki)
    # 케이스 출력
    print('#{}'.format(testcase))
    # 텍스트 나열 10개 단위로 줄 바꾸기
    for b in range(0, len(text), 10):
        print(text[b : b+10])  