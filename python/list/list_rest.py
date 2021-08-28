# 수 10개를 입력받은 뒤, 이를 각각 42로 나머지를 구한다
# 그 다음 서로 다른 값이 몇 개 있는 지 출력하는 프로그램
# 입력: 한 줄에 하나의 숫자가 주어진다
# 출력: 42로 각각 나눴을 때, 서로 다른 나머지가 몇 개 있는지 출력
num = []
for i in range(10):
    a = int(input())
    num.append(a % 42)
num = set(num)
print(len(num))