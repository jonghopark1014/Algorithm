def solution(lottos, win_nums):
    answer = []
    
    zero_cnt = lottos.count(0)
    correct = 0
    for i in win_nums:  
        if i in lottos:  
            correct += 1
    if correct + zero_cnt == 6:  
        answer.append(1)
    elif correct + zero_cnt == 5:  
        answer.append(2)
    elif correct + zero_cnt == 4:  
        answer.append(3)
    elif correct + zero_cnt == 3:  
        answer.append(4)
    elif correct + zero_cnt == 2:  
        answer.append(5)
    else:  
        answer.append(6)
    
    if correct == 6:  
        answer.append(1)
    elif correct == 5:  
        answer.append(2)
    elif correct == 4:  
        answer.append(3)
    elif correct == 3:  
        answer.append(4)
    elif correct == 2:  
        answer.append(5)
    else:  
        answer.append(6)
    
    return answer