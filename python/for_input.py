# 두 정수 A, B를 입력받은 후 A+B를 출력하는 프로그램
# 입력: 첫 줄에는 테스트 케이스 개수 T, 다음 줄부터 각 A, B가 주어진다
# 출력: 각 테스트 케이스마다 A+B 출력
T = int(input())
for i in range(1,T+1):
    A, B = map(int, input().split())
    print(A+B)