# 셀프 넘버
# 예시; d(75)=75+7+5=87/ n,d(n),d(d(n)),... 무한 수열
# 예시; 33, 33+3+3=39, 39+3+9=51,...
# n을 d(n)의 생성자라고 할 때, 생성자가 없는 숫자를 셀프 넘버라 한다
# 출력: 10000보다 작거나 같은 셀프 넘버를 한줄에 하나씩 출력
num_data = set(range(1, 10001))
generated_num = set()
for i in range(1,10001):    # i=850이면
    for j in str(i):        # j= "8","5","0"
        i = i + int(j)      # i=850+8+5+0
    generated_num.add(i)
self_num = sorted(num_data - generated_num)
for i in self_num:
    print(i)