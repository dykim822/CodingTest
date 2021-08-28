# 9개의 서로 다른 자연수가 주어질때, 최댓값을 찾고 그 최댓값이 몇번쨰 수인지 구하는 프로그램
# 입력: 1~9줄까지 한 줄에 하나의 자연수
# 출력: 첫줄에 최댓값, 둘째 줄에 몇 번째 수인지 출력
num_list = []
for i in range(9):
    num_list.append(int(input()))
print(max(num_list))
print(num_list.index(max(num_list))+1)