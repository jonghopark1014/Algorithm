A, B, C = map(int, input().split())
N = int(input())
A2 = N // 3600
B2 = (N % 3600) // 60
C2 = int((N % 3600) % 60)

A += A2
B += B2
C += C2

while C >= 60:
    C -= 60
    B += 1
    if B >= 60:
        A += 1
        B -= 60
        if A > 23:
            A -= 24
while B >= 60:
    A += 1
    B -= 60
    if A >= 24:
        A -= 24

while A >= 24:
    A -= 24

print(f'{A} {B} {C}')