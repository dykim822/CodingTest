# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램
# 입력: 첫 줄에 1이상 10000이하 n이 주어진다
# 출력: 1부터 n까지 합을 구한다
n = int(input())
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(sum)