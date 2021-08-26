# 첫 줄에는 별1개, 다음 줄은 2개, N번째 줄에는 N개 출력(단, 오른쪽 정렬)
# print(X.ljust(num))   왼쪽 정렬(자리수)
# print(X.rjust(num))   오른쪽 정렬
N = int(input())
for i in range(1, N+1):
    print(('*'*i).rjust(N))