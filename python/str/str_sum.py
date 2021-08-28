# N개의 숫자가 공백없이 출력되어 있을 때 숫자를 모두 합하는 프로그램
# 입력: 첫줄에 숫자 개수 N, 다음 줄에 숫자 N개가 공백없이 입력
# 출력: 숫자 N개의 합 출력
N = int(input())
num = input()
sum = 0
for i in num:
    sum += int(i)
print(sum)