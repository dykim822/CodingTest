# N개의 정수가 주어진다. 이때 최솟값과 최댓값을 구하는 프로그램
# 입력: 정수의 개수 N
# 출력: 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력
N = int(input())
A = list(map(int, input().split()))
#print('{} {}'.format(min(A), max(A)))
print('%d %d' %(min(A), max(A)))