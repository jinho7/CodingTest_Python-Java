def solution(absolutes, signs):
    for i, item in enumerate(signs):
        # i 가 True 일 때 (음수)
        if not item :
            absolutes[i] *= -1
    return sum(absolutes)

# zip을 이용한 풀이
# 여러 개의 이터러블(iterable, 반복 가능한 객체)을 인자로 받아 각 이터러블의 요소들을 튜플로 묶어 반환
def solution2(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer