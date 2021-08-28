# 한수; 어떤 양수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라 한다
# 입력: 1000이하 자연수 N
# 출력: 1이상 N이하의 한수의 개수를 출력
def solution(num):
    cnt = 0
    for i in range(1, num+1):
        num_list = list(map(int, str(i)))
        if i < 100:
            cnt += 1    # 100미만 수는 모두 한수
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            cnt += 1    # 등차수열 정의
    return cnt

N = int(input())
print(solution(N))