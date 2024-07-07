def solution(absolutes, signs):
    for i, item in enumerate(signs):
        # i 가 True 일 때 (음수)
        if not item :
            absolutes[i] *= -1
    return sum(absolutes)