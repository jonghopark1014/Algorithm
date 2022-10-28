T = int(input())

for tc in range(1, T+1):  
    # N K 구분
    N, K = map(int, input().split())
    # 평점 인원
    re_N = int(N / 10)
    # 전체 점수 빈리스트
    al_list = []
    # 랭크 리스트
    rank_po = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    # 점수를 빈 리스트에 넣음
    for i in range(N):  
        list_point = list(map(int, input().split()))
        al_list.append(list_point)

    # K번째 점수 평균 책정
    k_avr = al_list[K-1][0] * 0.35 + al_list[K-1][1] * 0.45 + al_list[K-1][2] * 0.2

    # 평균점수 리스트 만들고 정렬
    ave_list = []
    for j in range(len(al_list)):  
        ave_list.append((al_list[j][0] * 0.35 + al_list[j][1] * 0.45 + al_list[j][2] * 0.2))
    
    sort_ave = sorted(ave_list, reverse = True)
    # 딕셔너리에 등급과 점수 넣기
    grade_dic = {}
    K_grade = []
    # 등급 나누기
    for i in range(0, 10):  
        grade_dic[rank_po[i]] = sort_ave[re_N * i : re_N * (i+1)]
    
    for key, value in grade_dic.items():  
        K_grade.append(value)
    for l in range(len(K_grade)):  
        if k_avr in K_grade[l]:  
            print(f'#{tc} {rank_po[l]}')

