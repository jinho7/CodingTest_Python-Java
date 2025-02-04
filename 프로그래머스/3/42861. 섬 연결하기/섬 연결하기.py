import heapq

def solution(n, costs):
    # 인접행렬
    graph = [[0] *n for _ in range(n)]
    for s, e, c in costs:
        graph[s][e] = c
        graph[e][s] = c
         
    # (가중치, 시작 노드) 순! 최소힙 사용하기 위해
    heap = [ (0, 0) ]
    visited = [False] * n

    answer = 0
    
    while heap:
        cost, current = heapq.heappop(heap)
        
        if visited[current]:
            continue
        
        visited[current] = True
        answer += cost
        
        # 현재 노드와 연결된 간선들을 힙에 추가
        for next in range(n):
            if graph[current][next] != 0 and not visited[next]:
                heapq.heappush(heap, (graph[current][next], next))
    
    return answer