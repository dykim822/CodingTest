# 세자리 수 * 세자리 수 연산 과정(알고리즘)
#     12
# *   12
# =======
#     24
#    12
# =======
#    144
first=input()   # 첫번째수
second=input()  # 두번째수
first = int(first)
second = int(second)
third_line = first*(second % 10)
forth_line = first*((second // 10) % 10)
fifth_line = first*(second // 100)
sum = third_line+forth_line*10+fifth_line*100
print(third_line)
print(forth_line)
print(fifth_line)
print(sum)

# 별해
a = int(input())
b = input() # 문자로 취급
for number in b[::-1]:
    print(a*int(number))
print(a*int(b))