T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst_N = list(map(str, input().split()))
    if N % 2:
        mid = N//2
    else:
        mid = (N // 2) - 1
    A = lst_N[:mid+1]
    B = lst_N[mid+1:]
    result = []
    for i in range(len(B)):
        result.append(A[i])
        result.append(B[i])
    if len(A) != len(B):
        result.append(A[-1])
    print(f'#{tc}', *result)

