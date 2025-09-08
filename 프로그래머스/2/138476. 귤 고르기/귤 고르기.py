from collections import defaultdict
def solution(k, tangerine):
    tangerine_dict = defaultdict(int)
    
    # 1. 크기: 개수
    for t in tangerine:
        tangerine_dict[t] += 1
    
    # 2. 정렬 & 자르기 계산
    s = 0
    answer = 0
    for x in sorted(tangerine_dict.values(), reverse = True):
        s += x
        answer += 1
        if s >= k:
            return answer