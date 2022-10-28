i = 'CFF3FCCC0F3F3CF0333FC0CF0C3'
hexa = {
    'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15
}


code = ''
for j in range(len(i)):
    if i[j].isdigit():
        num = ''
        a = int(i[j])
        if a == 0:
            code += '0000'
        else:
            while True:
                if a == 1:
                    num += str(a)
                    break
                b = a % 2
                a = a // 2
                num += str(b)
            if len(num) < 4:
                num += '0' * (4-len(num))
            num = num[::-1]
            code += num
        len_code = len(code)
    else:
        num = ''
        a = hexa[i[j]]
        while True:
            if a == 1:
                num += str(a)
                break
            b = a % 2
            a = a // 2
            num += str(b)
        if len(num) < 4:
            num += '0' * (4 - len(num))
        num = num[::-1]
        code += num
        len_code = len(code)

print(len(code))
print(code)