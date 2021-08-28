# 기말고사 과목 수 N, 과목 중 최댓값 M
# 모든 점수를 과목점수/M*100으로 고쳤다
# 새로운 평균을 구하는 프로그램
# 입력: 첫줄에는 과목 갯수 N, 둘째줄에는 과목 점수
# 출력: 새로운 평균 출력
N = int(input())
score_before = list(map(int, input().split()))
M = max(score_before)
score_after = []
for i in score_before:
    score_after.append(i/M *100)
avg = sum(score_after) / N
print(avg)