from collections import deque

def solution(maps):

    # 5 x 5 고정이긴 한데, 형식적으로
    n = len(maps)
    m = len(maps[0])
    
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = [[False] * m for _ in range(n)]
    
    queue = deque()
    queue.append([0, 0, 1])
    visited[0][0] = True
    
    def bfs():
        while queue:
            x, y, distance = queue.popleft()
            
            # 끝 (도착점에 도착)
            if x == n-1 and y == m-1:
                return distance
            
            # 상하좌우
            for dx, dy in direction:
                nx = x + dx
                ny = y + dy
                
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True  # 방문 처리
                    queue.append([nx, ny, distance + 1])  # 다음 탐색할 위치 및 거리 추가
        # 경로 없다면
        return -1
    
    return bfs()  # BFS 탐색 결과 반환
