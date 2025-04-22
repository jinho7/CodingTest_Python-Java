import heapq

def solution(N, road, K):
    answer = 0
    # 2차원 배열로 하면 X
    # hash에다가 길 저장
    dic = { i : [] for i in range(N) }
    
    for x, y, weight in road:
        dic[x-1].append((y-1, weight))
        dic[y-1].append((x-1, weight))
        
    def dijkstra():
        distances = [float('inf') for _ in range(N)]
    
        # distance, node 순 (max_heap)
        heap = [(0, 0)]
        distances[0] = 0
        while heap:
            dist, c_node = heapq.heappop(heap)
            # 모든 노드 검색
            for n_node, weight in dic[c_node]:
                # 연결된 노드 거르기
                if weight > 0 :
                    n_dist = dist + weight
                    if n_dist < distances[n_node]:
                        distances[n_node] = n_dist
                        heapq.heappush(heap, (n_dist, n_node))
        return distances
    
    temp = dijkstra()

    for x in range(len(temp)):
        if temp[x] <= K:
            answer += 1
    return answer