# 주어진 좌표가 어느 사분면에 속하는지 출력하는 프로그램
# 첫 줄에는 정수x, 다음 줄에는 정수y 입력
# 사분면 번호를 출력
x = int(input())
y = int(input())
if x>0 and x!=0 and y!=0:
    if y>0:
        print(1)
    else:
        print(4)
else:
    if y>0:
        print(2)
    else:
        print(3)