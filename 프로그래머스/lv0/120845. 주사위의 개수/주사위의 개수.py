def solution(box, n):
    answer = 0
    for i in box:  
        if not answer:  
            answer = i // n
        else:  
            answer *= i // n
    return answer