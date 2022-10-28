# 자릿수 더하기
def add_digit(number):  
    return sum(list(map(int, list(number))))

# 출력
if __name__ == '__main__':  
    number = input()
    print(add_digit(number))
