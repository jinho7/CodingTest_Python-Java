import heapq

def solution(n, k, enemy):
    max_heap = []
    
    for i in range(len(enemy)):
        # 매 라운드마다 적의 수 차감
        n -= enemy[i]
        # 음수 -> 최대 힙
        heapq.heappush(max_heap, -enemy[i])
        
        # 병사가 부족해진 경우
        if n < 0:
            # 무적권이 있
            if k > 0:
                # 가장 큰 적의 수를 무적권으로 처리 & 병사 수 되돌림
                n += -heapq.heappop(max_heap)
                k -= 1
            else:
                # 현재 라운드
                return i
    
    # 모든 라운드를 막을 수 있으면 라운드의 수 반환
    return len(enemy)