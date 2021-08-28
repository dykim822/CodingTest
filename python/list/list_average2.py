# 입력: 테스트 케이스
# 두번째 줄: 케이스마다 학생수N 이어서 N명의 점수
# 출력: 한 줄씩 평균을 넘는 학생들의 비율을 반올림해서 소수 셋째자리까지 출력
T = int(input())
for i in range(T):
    case = list(map(int, input().split()))
    avg = sum(case[1:]) / case[0]
    cnt = 0
    for score in case[1:]:
        if score > avg:
            cnt += 1
    rate = cnt / case[0] * 100
    print('%.3f%%' %(rate))
    #print(f'{rate:.3f}%')