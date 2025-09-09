from collections import deque, defaultdict
import heapq

def solution(priorities, location):
    # OS Scheduler Rules
    # 1. 대기 큐에서 하나 꺼내기
    # 2. 대기 큐에 우선 순위가 더 높은 것이 있다면 다시 뒤로 넣기
    
    dic = defaultdict(int)
    q = deque([])
    heap = []
    for i in range(len(priorities)):
        dic[i] = priorities[i]
        q.append(i)
        heapq.heappush(heap, -priorities[i])
    
    answer = 0
    
    while q:
        # 맨 앞에 꺼 뺌
        x = q.popleft()
        # 그의 우선순위
        x_priority = dic[x]

        # 최고 우선순위라면, 실행
        max_priority = -heapq.heappop(heap)
        if x_priority >= max_priority:
            answer += 1
            if x == location:
                return answer
        # 아니라면 다시 넣기
        else:
            q.append(x)
            heapq.heappush(heap, -max_priority)
        
    return answer