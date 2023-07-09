words = []
max_v = 0

for i in range(5):
    a = input()
    words.append(a)
    max_v = max(max_v, len(a))

for j in range(max_v):
    for k in range(5):
        try:
            print(words[k][j], end="")
        except:
            pass
