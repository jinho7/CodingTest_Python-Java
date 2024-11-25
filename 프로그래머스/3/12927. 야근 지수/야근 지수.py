import heapq

def solution(n, works):
#     # 제곱은 밑의 크기가 커질수록 커짐
#     # 최대한 고르게 분배하는 방법.
#     if sum(works) <= n :
#         return 0
        
#     left = sum(works) - n
#     base = left // len(works)
#     # base와 base+1인 것으로 이루어져 있음
#     # 둘의 개수를 찾아서 제곱해주면 끝
#     remain = left % len(works)
    
#     answer = (base**2) * len(works) - remain + ((base+1)**2) * remain
    
    # =============== 오답 노트 =====================
    # 한번에 균등 분배할 수 없고
    # 1씩 줄여가면서 점진적으로 균등해지도록 해야 한다...
    # 반례 : Case: works = [5, 1, 1, 1], n = 2

    works = [-work for work in works]
    heapq.heapify(works)
    i = 0
    while i != n :
        i += 1
        if works:
            x = heapq.heappop(works)
        if x != 0:
            heapq.heappush(works, (x+1))
    answer = sum([work**2 for work in works])
    return answer