from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    # 상하좌우에 대한 directions 도 정의 (for 문으로 모두 탐색할 거임)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # deque 사용 -> x,y 넣어줘야하고, 그리고 거리도 넣어줘야 됨.
    queue = deque([(0, 0, 1)])
    
    # 방문 기록
    visited = [[False] * m for _ in range(n)]
    
    def bfs():
        while queue:
            x, y, distance = queue.popleft()
            
            # 목적지 도착하면 끝.
            if x == n-1 and y == m-1:
                return distance
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # 범위 확인, 길 확인, 방문 확인
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx, ny, distance + 1))
                    visited[nx][ny] = True
        
        return -1
    
    return bfs()