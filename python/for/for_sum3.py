# 두 정수 A,B를 입력받은 다음 A+B 출력 프로그램
# 단, 출력 시 "Case #x:" 를 출력하고 A+B출력
T = int(input())
for i in range(1,T+1):
    A, B = map(int, input().split())
    print('Case #%d: %d' %(i, A+B))
    #print('Case #{}: {}'.format(i, A+B))