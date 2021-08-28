# 세 개의 자연수 A,B,C가 주어질 때 A*B*C를 계산한 결과에 0부터 9까지 각 숫자가 몇번씩 사용되었는지 출력하는 프로그램
# 입력: 첫줄에 A, 둘째줄에 B, 셋째줄에 C
# 출력: 첫줄에 0이 몇번 사용되었는지, 다음줄에는 1, ... 총 10줄 출력
A = int(input())
B = int(input())
C = int(input())
result = list(str(A*B*C))
for i in range(10):
    print(result.count(str(i)))