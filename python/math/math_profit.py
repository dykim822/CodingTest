# 손익분기점 구하는 프로그램
# 노트북 판매 대수에 상관없이 매년 임대료, 재산세, 보험료, 급여 등 A만원의 고정비용 발생
# 한 대의 노트북 생산 시 재료비+인건비 등 총 B만원의 가변 비용 발생
# 예시) A=1000만원, B=70만원 일때 한대 생산비용=1070만원, 열대 생산시 1700만원
# 노트북 가격이 C만원으로 책정/ 총 수입(판매비용) >= 총 생산 비용 인 순간의 지점을 손익분기점
def solution(A, B, C):
    if B >= C:
        cnt = -1
    else:
        cnt = A//(C-B) + 1
    return print(cnt)

solution(2100000000,9,10)