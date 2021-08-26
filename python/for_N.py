# 자연수 N이 주어졌을 때 1부터 N까지 한줄에 하나씩 출력하는 프로그램
# 입력: 자연수 N
# 출력: 첫 줄부터 N번째 줄까지 차례대로 출력
N = int(input())
for i in range(1,N+1):  # range(N); 0부터 N미만까지, 즉 N개
    print(i)