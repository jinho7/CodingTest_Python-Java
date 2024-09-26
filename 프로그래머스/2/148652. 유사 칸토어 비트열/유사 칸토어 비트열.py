import math

def solution(n, l, r):
    # 0: 1
    # 1: 1 -> 11011
    # 2: 11011 11011 00000 11011 11011
    # 3: {125개}
    # 마치 세포 분열 같구먼, 계속 5단계로 나눠짐.
    # 1 -> 5개, 2 -> 25개, n -> 5의 n승 개
    # 5로 계속 나누면서 가운데는 버리고 계속 계산
    answer = 0
    
    for i in range(l-1,r):
        # 5로 계속 나누기
        while i > 0:
            i, mod = divmod(i, 5)
            if mod == 2:
                break
        else:
            answer += 1
    return answer