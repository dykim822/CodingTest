# 90~100은 A, 80~89점은 B, 70~79점은 C, 60~69점은 D, 나머지 점수는 F
score = int(input())
if score >= 90 and score <= 100:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# if 90<=score<=100:
#     print("A")
# elif 80<=score<=89:
#     print("B")
# elif 70<=score<=79:
#     print("C")
# elif 60<=score<=69:
#     print("D")
# elif 0<=score<60:
#     print("F")