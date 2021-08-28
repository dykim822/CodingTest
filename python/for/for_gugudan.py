# N을 입력받은 뒤, 구구단 N단 출력
# 입력: 자연수N, 1이상 9이하
# 출력: N*1 부터 N*9까지 출력
N = int(input())
if 1<= N <= 9:
    for i in range(1,10):
        print('%d * %d = %d' %(N, i, N*i))
#        print(N,'*',i,'=',N*i)
else:
    pass