# map 함수
# a = list(map(int, a)) => int(a[0]) int(a[1]) int(a[2]) ... 생성
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)
a = input().split()
print(a)    # ['입력', '입력'] 리스트로 반환
b = map(int, input().split())
print(b)
print(list(b))
c, d = map(int, input().split())
print(c)
print(d)
print(c+d)