# 자연수 N이 주어졌을 때 N부터 1까지 한줄에 하나씩 출력하는 프로그램
# 입력: 자연수 N
# 출력: 첫 줄부터 N번째 줄까지 차례대로 출력
N = int(input())
for i in range(N,0,-1):
    print(i)