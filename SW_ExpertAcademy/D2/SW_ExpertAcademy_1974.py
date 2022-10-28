T = int(input())

for tc in range(1, T+1):  
    puzzle = []
    TF_V = 1
    # 스도쿠 만들기
    for i in range(9):  
        N = list(map(int, input().split()))
        puzzle.append(N)

    # 가로 검사
    for j in puzzle:  
        if len(set(j)) != 9:  
            TF_V = 0
    
    # 세로검사
    c_puzzle = list(zip(*puzzle))
    for k in c_puzzle:  
        if len(set(k)) != 9:  
            TF_V = 0
    
    # 칸 검사
    for n in range(0, 9, 3):  
        o_puzzle = []
        p_puzzle = []
        q_puzzle = []
        for l in range(n, n+3):  
            for m in range(0, 3):  
                o_puzzle.append(puzzle[l][m])
        if len(set(o_puzzle)) != 9:  
                TF_V = 0

        for l in range(n, n+3):  
            for m in range(3, 6):  
                p_puzzle.append(puzzle[l][m])
        if len(set(o_puzzle)) != 9:  
                TF_V = 0
        
        for l in range(n, n+3):  
            for m in range(6, 9):  
                q_puzzle.append(puzzle[l][m])
        if len(set(q_puzzle)) != 9:  
                TF_V = 0
            
    print(f'#{tc} {TF_V}')
            

        
    