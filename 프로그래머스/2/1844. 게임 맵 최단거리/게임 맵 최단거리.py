from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    def bfs(x, y):
        queue = deque([(x, y, 1)])
        visited = set()
        visited.add((x,y))
        
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        
        # queue가 다 빌 때까지
        while queue:
            x, y, distance = queue.popleft()
            
            if x == n-1 and y == m-1:
                return distance
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and (nx, ny) not in visited:
                    queue.append((nx, ny, distance + 1))
                    visited.add((nx, ny))
        return -1
    
    return bfs(0, 0)