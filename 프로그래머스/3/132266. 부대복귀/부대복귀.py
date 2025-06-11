from collections import defaultdict, deque

def solution(n, roads, sources, destination):
    # graph 표기
    graph = defaultdict(list)
    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)
        
    # 각 sources들에서 dsstination으로 복귀하는 최단 시간을 return 하는 bfs 함수
    # 가 아니라, destination으로 시작해서 각 지점을 다 저장
    dist = [-1] * (n + 1)
    queue = deque([(destination)])
    dist[destination] = 0

    while queue:
        curr = queue.popleft()
        for neighbor in graph[curr]:
            # 처음 방문
            if dist[neighbor] == -1:
                dist[neighbor] = dist[curr] + 1
                queue.append((neighbor))
    
    return [dist[s] for s in sources]