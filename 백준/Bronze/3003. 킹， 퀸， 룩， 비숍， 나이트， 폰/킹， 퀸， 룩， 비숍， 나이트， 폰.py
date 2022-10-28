import sys

piece = [1, 1, 2, 2, 2, 8]
my_piece = list(map(int, sys.stdin.readline().split()))

for i in range(len(piece)):  
    piece[i] = piece[i] - my_piece[i]

for j in piece:  
    print(j)