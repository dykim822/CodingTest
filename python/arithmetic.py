# 두 자연수 A, B 입력 후 A+B, A-B, A*B, A/B, A%B 출력 프로그램
A, B = map(int, input().split())
print(A+B)
print(A-B)
print(A*B)
print(int(A/B)) # print(A//B)
print(A%B)

# map 함수 사용하지 않을 때
A, B = input().split()
A = int(A)
B = int(B)
print(A+B, A-B, A*B, A//B, A%B, sep='\n')