# A, B 가위바위보 분리
A, B = map(int, input().split())

#가위 바위 보 리스트
xyz = {1:'가위', 2:'바위', 3:'보'}

#가위 바위 보 승리 조건 설정
if xyz[A] == ' 가위' and xyz[B] == '보':  
    print('A')
elif xyz[A] == '바위' and xyz[B] == '가위':  
    print('A')
elif xyz[A] == '보' and xyz[B] == '바위':  
    print('A')
else:  
    print('B')
