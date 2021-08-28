# 두 정수 A,B를 입력받은 다음 A+B 출력 프로그램
# 단, 출력 시 "Case #x: A + B = C" 형식으로 출력한다!
# x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.
T = int(input())
for i in range(1, T+1):
    A,B = map(int, input().split())
    print('Case #%d: %d + %d = %d' %(i,A,B,A+B))
    #print('Case #{}: {} + {} = {}'.format(i,A,B,A+B))