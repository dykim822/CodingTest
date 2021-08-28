# OX 퀴즈/ OX퀴즈 점수를 구하는 프로그램/ 문제를 맞은 경우 그 점수는 그 문제까지 연속된 O의 개수
# 입력: 테스트 케이스 개수/ 테스트 케이스는 한줄로 구성
# 출력: 각 테스트 케이스마다 점수 출력
T = int(input())
for i in range(T):
    a = input()
    sum = 0
    score = 0
    for ox in a:
        if ox == 'O':
            score += 1
        else:
            score = 0
        sum += score
    print(sum)