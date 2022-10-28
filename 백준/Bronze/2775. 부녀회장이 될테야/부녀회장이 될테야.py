import sys

T = int(sys.stdin.readline())

for tc in range(1, T+1):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    temp_l = [i for i in range(1, n+1)]
    result_l = [1] + ([0] * (n-1))
    sumV = 0
    if k == 0:
        print(n)
    else:
        for _ in range(k):
            for i in range(1, n):
                for j in range(i+1):
                    sumV += temp_l[j]
                result_l[i] = sumV
                sumV = 0
            temp_l = result_l[:]
        print(result_l[-1])