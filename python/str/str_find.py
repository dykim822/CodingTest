# 알파벳 소문자로만 이뤄진 단어 S
# 각각의 알파벳에 대해서, 단어에 포함된 경우에는 처음 등장하는 위치를
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성
# 입력: 첫줄에 단어 S
# 출력: a가 처음 등장하는 위치, b가 처음 등장하는 위치, ...., z가 처음 등장하는 위치를 공백으로 구분해서 출력
# 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력, 단어의 첫글자는 0번째
# 예시 입력: baekjoon
# 예시 출력: 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
S = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabet:
    if i in S:
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')