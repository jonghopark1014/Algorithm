import sys

total_price = int(sys.stdin.readline())
N = int(sys.stdin.readline())
comp_price = 0
for i in range(N):
    price, cnt = map(int, sys.stdin.readline().split())
    comp_price += price*cnt

if total_price == comp_price:
    print('Yes')
else:
    print('No')