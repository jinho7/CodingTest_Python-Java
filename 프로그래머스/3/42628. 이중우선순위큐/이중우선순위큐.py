import heapq
from collections import defaultdict

def solution(operations):
    min_heap = []
    max_heap = []
    num_dict = defaultdict(int)  # 각 숫자의 개수를 추적
    
    for operation in operations:
        op, num = operation.split()
        num = int(num)  # 문자열을 정수로 변환
        
        # 명령어 I
        if op == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            num_dict[num] += 1
            
        # 명령어 D
        else:
            if not min_heap:  # 힙이 비어있으면 skip
                continue
                
            # 최댓값 삭제 (D 1)
            if num == 1:
                # 유효한 최댓값 찾기
                while max_heap and num_dict[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    max_num = -heapq.heappop(max_heap)
                    num_dict[max_num] -= 1
                    
            # 최솟값 삭제 (D -1)
            else:
                # 유효한 최솟값 찾기
                while min_heap and num_dict[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    min_num = heapq.heappop(min_heap)
                    num_dict[min_num] -= 1
    
    # 최종 결과 계산
    # 남아있는 유효한 값 찾기
    while min_heap and num_dict[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and num_dict[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
        
    if not min_heap:  # 큐가 비어있는 경우
        return [0, 0]
    
    # 최댓값과 최솟값 반환
    return [-max_heap[0], min_heap[0]]