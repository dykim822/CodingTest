# 알람시계 프로그램
# 입력: 첫 줄에 두 정수 시간H, 분M이 주어진다/ 24시간 표현
# 출력: 입력 시간보다 45분 일찍 알람 설정할 시각
H, M = map(int, input().split())
if 0<= H <=23 and 0<= M <= 59:
    if M >= 45:
        if H==0:
            print('%d %d' %(H, M-45))
        else:
            print('%d %d' %(H, M-45))
    else:
        if H==0:
            print('%d %d' %(24+H-1, 60+M-45))
        else:
            print('%d %d' %(H-1, 60+M-45))
else:
    pass