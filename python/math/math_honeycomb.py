# 육각형으로 이뤄진 벌집이 있다.
def honeycomb(N):
    init = 1
    cnt = 1
    while N > init:
         init += 6*cnt
         cnt += 1
    return print(cnt)

honeycomb(58)