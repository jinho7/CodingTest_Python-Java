# 힙 사용 안하면 못 풀겠다 싶어서 조금 참고함.
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    sum = 0
    max = len(scoville)-1
    
    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        if sum == max:
            return -1
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        sum += 1
        
    return sum
    