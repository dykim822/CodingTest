# 입출력 방식 개선 방법
# Python의 경우 input이용 시 시간초과과 발생할 수 있기에 sys.stdin.readline 사용한다
# 단 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우
# .rstrip()을 추가로 해주는 것이 좋다!
import sys
T = int(input())
for i in range(1,T+1):
    A,B = map(int,sys.stdin.readline().split())
    print(A+B)